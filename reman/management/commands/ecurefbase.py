from django.core.management.base import BaseCommand
from django.core.management.color import no_style
from django.db import connection
from django.db.utils import DataError

from reman.models import EcuRefBase, EcuModel, SparePart
from utils.conf import XLS_ECU_REF_BASE

from ._excel_reman import ExcelEcuRefBase

import logging as log


class Command(BaseCommand):
    help = 'Interact with the EcuRefBase table in the database'

    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('sheet_id', type=int)

        parser.add_argument(
            '-f',
            '--file',
            dest='filename',
            help='Specify import Excel file',
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            dest='delete',
            help='Delete all data in EcuRefBase table',
        )

    def handle(self, *args, **options):
        if options['delete']:
            EcuRefBase.objects.all().delete()
            EcuModel.objects.all().delete()

            sequence_sql = connection.ops.sequence_reset_sql(no_style(),
                                                             [EcuRefBase, EcuModel])
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)
            self.stdout.write(self.style.WARNING("Suppression des données de la table EcuRefBase terminée!"))
        else:
            if options['filename'] is not None:
                extraction = ExcelEcuRefBase(options['filename'], sheet_name=options['sheet_id'])
            else:
                extraction = ExcelEcuRefBase(XLS_ECU_REF_BASE, sheet_name=options['sheet_id'])

            nb_base_before, nb_ecu_before = EcuRefBase.objects.count(), EcuModel.objects.count()
            nb_base_update, nb_ecu_update, nb_part_update = 0, 0, 0
            for row in extraction.read_all():
                log.info(row)
                reman_reference = row["reman_reference"]
                code_produit = row["code_produit"]
                del row["reman_reference"]
                del row["code_produit"]
                try:
                    # Update or Create SpareParts
                    part_obj, part_created = SparePart.objects.update_or_create(
                        code_zone="REMAN PSA", code_produit=code_produit
                    )
                    if not part_created:
                        nb_part_update += 1

                    # Update or Create EcurefBase
                    base_obj, base_created = EcuRefBase.objects.update_or_create(reman_reference=reman_reference)
                    if not base_created:
                        nb_base_update += 1

                    # Update or Create Ecumodel
                    ecu_obj, ecu_created = EcuModel.objects.update_or_create(
                        spare_part=part_obj, ecu_ref_base=base_obj, **row
                    )
                    if not ecu_created:
                        nb_ecu_update += 1
                except DataError as err:
                    print("DataError: {} - {}".format(reman_reference, err))
            nb_base_after, nb_ecu_after = EcuRefBase.objects.count(), EcuModel.objects.count()
            self.stdout.write(
                self.style.SUCCESS(
                    "EcuRefBase data update completed: CSV_LINES = {} | ADD = {} | UPDATE = {} | TOTAL = {}".format(
                        extraction.nrows, nb_base_after - nb_base_before, nb_base_update, nb_base_after
                    )
                )
            )
            self.stdout.write(
                self.style.SUCCESS(
                    "EcuModel data update completed: CSV_LINES = {} | ADD = {} | UPDATE = {} | TOTAL = {}".format(
                        extraction.nrows, nb_ecu_after - nb_ecu_before, nb_ecu_update, nb_ecu_after
                    )
                )
            )