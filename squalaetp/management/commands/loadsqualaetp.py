from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.core.management import call_command
from django.core.exceptions import ObjectDoesNotExist
from django.db import connection

from squalaetp.models import Xelon
from psa.models import Corvet


class Command(BaseCommand):
    help = 'Interact with the Squalaetp tables in the database'

    def add_arguments(self, parser):
        parser.add_argument(
            '-f',
            '--file',
            dest='filename',
            help='Specify import Excel file',
        )
        parser.add_argument(
            '--relations',
            action='store_true',
            dest='relations',
            help='add the relationship between the xelon and corvet tables',
        )
        parser.add_argument(
            '--del_relations',
            action='store_true',
            dest='del_relations',
            help='delete all relations',
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete all data in Squalaetp tables',
        )

    def handle(self, *args, **options):
        self.stdout.write("[SQUALAETP] Waiting...")

        if options['relations']:
            self._foreignkey_relation()

        elif options['delete']:
            Xelon.objects.all().delete()
            Corvet.objects.all().delete()

            sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Xelon, Corvet, ])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)
            for table in ["Xelon", "Corvet", "CorvetBackup"]:
                self.stdout.write(self.style.WARNING("Suppression des données de la table {} terminée!".format(table)))

        else:
            call_command("loadraspeedi")
            call_command("programing")
            call_command("corvet")
            call_command("xelon", "--fix_update")
            call_command("indicator")

    def _foreignkey_relation(self):
        self.stdout.write("[SQUALAETP_RELATIONSHIPS] Waiting...")

        nb_xelon, nb_corvet, objects_list = 0, 0, []
        for xelon in Xelon.objects.filter(corvet__isnull=True):
            try:
                xelon.corvet = Corvet.objects.get(pk=xelon.vin)
                xelon.save()
                nb_xelon += 1
            except ObjectDoesNotExist:
                objects_list.append(xelon.numero_de_dossier)
        self.stdout.write(
            self.style.SUCCESS(
                "[SQUALAETP] Relationships update completed: CORVET/XELON = {} | RASPEEDI/CORVET = {}".format(
                    nb_xelon, nb_corvet
                )
            )
        )