from django.utils import unittest
from django.test import Client

from yaproject.vcard.models import VCard, RequestStore


class VcardModelsTest(unittest.TestCase):
    def test_vcard_with_data(self):
        self.vcard = VCard.objects.get(pk=1)
        self.assertTrue(self.vcard.name)
        self.assertTrue(self.vcard.surname)
        self.assertTrue(self.vcard.birth_date)
        self.assertTrue(self.vcard.bio)
        self.assertTrue(self.vcard.e_mail)

    def test_vcard_with_unicode(self):
        self.vcard = VCard.objects.get(pk=1)
        self.assertEqual('Yaroslav Tsarevsky', self.vcard.__unicode__())


class AdminTest(unittest.TestCase):
    def test_admin_with_vcard(self):
        client = Client()
        self.resp = client.get('/admin/vcard/vcard/')
        self.assertEqual(self.resp.status_code, 200)


class VcardViewsTest(unittest.TestCase):
    def test_views_with_contacts(self):
        client = Client()
        self.resp = client.get('/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertTrue(self.resp.context['contacts'])


class RequestStoreTest(unittest.TestCase):
    def test_middleware_with_store(self):
        client = Client()
        self.resp = client.get('/request_store/')
        self.assertEqual(self.resp.status_code, 200)
        self.req_store = RequestStore.objects.latest('date')
        self.assertTrue(self.req_store)
        self.assertTrue(self.req_store.host)
        self.assertTrue(self.req_store.path)
