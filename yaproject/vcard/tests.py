from django.utils import unittest
from django.test import Client
from django.template import RequestContext
from django.test.client import RequestFactory
from django.conf import settings as django_settings
from yaproject.vcard.context_processor import add_settings

from yaproject.vcard.models import VCard, RequestStore


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


class RequestStoreTest(unittest.TestCase):
    def testMiddleware(self):
        client = Client()
        self.resp = client.get('/request_store/')
        self.assertEqual(self.resp.status_code, 200)
        self.req_store = RequestStore.objects.latest('date')
        self.assertTrue(self.req_store)


class ContextProcessorTest(unittest.TestCase):
    def test_settings(self):
        factory = RequestFactory()
        request = factory.get('/')
        c = RequestContext(request, {'foo': 'bar'}, [add_settings])
        self.assertTrue('settings' in c)
        self.assertEquals(c['settings'], django_settings)
