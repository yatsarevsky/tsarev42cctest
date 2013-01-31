from django.utils import unittest
from django.test import Client

from yaproject.vcard.models import VCard


class VcardModelsTest(unittest.TestCase):
    def testDataInfo(self):
        self.vcard = VCard.objects.get(pk=1)
        self.assertTrue(self.vcard.name)
        self.assertTrue(self.vcard.surname)
        self.assertTrue(self.vcard.birth_date)
        self.assertTrue(self.vcard.bio)
        self.assertTrue(self.vcard.e_mail)

    def setUp(self):
        self.vcard = VCard.objects.create(
            name='test',
            surname='test',
            birth_date='1985-06-17',
            bio='test',
            e_mail='test@test.ru')

    def test_vcard_unicode(self):
        self.assertEqual('test test', self.vcard.__unicode__())


class AdminTest(unittest.TestCase):
    def testVCard(self):
        client = Client()
        self.resp = client.get('/admin/vcard/vcard/')
        self.assertEqual(self.resp.status_code, 200)


class VcardViewsTest(unittest.TestCase):
    def testContacts(self):
        client = Client()
        self.resp = client.get('/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertTrue(self.resp.context['contacts'])
