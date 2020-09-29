from django.urls import reverse
from django.contrib.messages import get_messages
from django.utils.translation import ugettext as _

from dashboard.tests.base import UnitTest

from reman.models import Repair, SparePart, Batch, EcuModel, EcuRefBase, EcuType


class RemanTestCase(UnitTest):

    def setUp(self):
        super(RemanTestCase, self).setUp()
        self.psaBarcode = '9612345678'
        spare_part = SparePart.objects.create(code_produit='test HW_9876543210')
        ecu_type = EcuType.objects.create(hw_reference='9876543210', technical_data='test', spare_part=spare_part)
        ref_base = EcuRefBase.objects.create(reman_reference='1234567890', ecu_type=ecu_type)
        ecu = EcuModel.objects.create(oe_raw_reference='1699999999', ecu_type=ecu_type, psa_barcode=self.psaBarcode)
        batch = Batch.objects.create(year="C", number=1, quantity=10, created_by=self.user, ecu_ref_base=ref_base)
        self.repair = Repair.objects.create(batch=batch, identify_number="C001010001", created_by=self.user)

    def test_repair_table_page(self):
        url = reverse('reman:repair_table')
        response = self.client.get(url)
        self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

        # Test if connected with permissions
        self.add_perms_user(Repair, 'view_repair')
        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_spare_part_table_page(self):
        url = reverse('reman:part_table')
        response = self.client.get(url)
        self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

        self.add_perms_user(SparePart, 'view_sparepart')
        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_repair_pages(self):
        urls_perms = [
            (reverse('reman:create_repair'), 'add_repair'),
            (reverse('reman:edit_repair', kwargs={'pk': self.repair.pk}), 'change_repair'),
            (reverse('reman:close_repair', kwargs={'pk': self.repair.pk}), 'change_repair'),
            (reverse('reman:detail_repair', kwargs={'pk': self.repair.pk}), 'view_repair'),
        ]
        for url, perm in urls_perms:
            response = self.client.get(url)
            self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

            self.add_perms_user(Repair, perm)
            self.login()
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.client.logout()

    def test_batch_table(self):
        url = reverse('reman:batch_table')
        response = self.client.get(url)
        self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

        self.add_perms_user(Batch, 'view_batch')
        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_out_table(self):
        url = reverse('reman:out_table')
        response = self.client.get(url)
        self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

        self.add_perms_user(Repair, 'close_repair')
        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Invalid form
        response = self.client.post(url, {'identify_number': ''})
        self.assertFormError(response, 'form', 'identify_number', _('This field is required.'))
        for identify_number in ['C001010001', 'C001010001R']:
            response = self.client.post(url, {'identify_number': identify_number})
            self.assertFormError(response, 'form', 'identify_number', "N° d'identification invalide")

    def test_check_part(self):
        url = reverse('reman:part_check')
        response = self.client.get(url)
        self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

        self.add_perms_user(EcuModel, 'check_ecumodel', 'add_ecumodel')
        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        # Invalid form
        response = self.client.post(url, {'psa_barcode': ''})
        self.assertFormError(response, 'form', 'psa_barcode', _('This field is required.'))
        for barcode in ['123456789', 'abcdefghij', '96123', '981234567']:
            response = self.client.post(url, {'psa_barcode': barcode})
            self.assertFormError(response, 'form', 'psa_barcode', _('PSA barcode is invalid'))

        # Valid form
        for barcode in ['9600000000', '9687654321', '9800000000', '9887654321']:
            response = self.client.post(url, {'psa_barcode': barcode})
            self.assertRedirects(
                response, reverse('reman:create_ref_base', kwargs={'psa_barcode': barcode}), status_code=302)
        response = self.client.post(url, {'psa_barcode': self.psaBarcode})
        ecu = EcuModel.objects.get(psa_barcode=self.psaBarcode)
        self.assertEquals(response.context['ecu'], ecu)

    def test_new_part_email(self):
        url = reverse('reman:part_email', kwargs={'psa_barcode': self.psaBarcode})
        response = self.client.get(url)
        self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

        self.add_perms_user(EcuModel, 'check_ecumodel')
        self.login()
        response = self.client.get(url)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), _('Success: The email has been sent.'))
        self.assertRedirects(response, reverse('reman:part_check'), status_code=302)

    def test_ecu_ref_base_table(self):
        url = reverse('reman:ecu_table')
        response = self.client.get(url)
        self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

        self.add_perms_user(EcuRefBase, 'view_ecurefbase')
        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_ecu_dump_table(self):
        url = reverse('reman:ecu_dump_table')
        response = self.client.get(url)
        self.assertRedirects(response, self.nextLoginUrl + url, status_code=302)

        self.add_perms_user(EcuRefBase, 'view_ecurefbase')
        self.login()
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
