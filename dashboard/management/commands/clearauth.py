from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.db import connection
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Clear Auth tables'

    def add_arguments(self, parser):
        parser.add_argument(
            '--group',
            action='store_true',
            dest='group',
            help='Clear Group table',
        )
        parser.add_argument(
            '--permission',
            action='store_true',
            dest='permission',
            help='Clear Permission table',
        )

    def handle(self, *args, **options):
        if options['group']:
            Group.objects.all().delete()
            Group.permissions.through.objects.all().delete()

            sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Group, Group.permissions.through, ])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)
            for table in ["Group"]:
                self.stdout.write(self.style.SUCCESS("Suppression des données de la table {} terminée!".format(table)))
        if options['permission']:
            Permission.objects.all().delete()

            sequence_sql = connection.ops.sequence_reset_sql(no_style(), [Permission, ])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)
            for table in ["Permission"]:
                self.stdout.write(self.style.SUCCESS("Suppression des données de la table {} terminée!".format(table)))
