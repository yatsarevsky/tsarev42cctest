from django.utils import unittest
from django.test import Client
from django.template import RequestContext
from django.test.client import RequestFactory
from django.conf import settings as django_settings
from yaproject.vcard.context_processor import add_settings

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
        self.vcard = self.resp.context['contacts']
        self.assertTrue(self.vcard.name)
        self.assertTrue(self.vcard.surname)
        self.assertTrue(self.vcard.birth_date)
        self.assertTrue(self.vcard.bio)
        self.assertTrue(self.vcard.e_mail)

    def test_views_with_edit_page(self):
        pass

    def test_views_with_registration(self):
        pass

    def test_views_with_login(self):
        pass

    def test_views_with_logout(self):
        pass


class RequestStoreTest(unittest.TestCase):
    def test_middleware_with_store(self):
        client = Client()
        self.resp = client.get('/request_store/')
        self.assertEqual(self.resp.status_code, 200)
        self.req_store = RequestStore.objects.latest('date')
        self.assertTrue(self.req_store)
        self.assertTrue(self.req_store.host)
        self.assertTrue(self.req_store.path)


class ContextProcessorTest(unittest.TestCase):
    def test_context_processor_with_settings(self):
        factory = RequestFactory()
        request = factory.get('/')
        c = RequestContext(request, {'foo': 'bar'}, [add_settings])
        self.assertTrue('settings' in c)
        self.assertEquals(c['settings'], django_settings)


class FormTest(unittest.TestCase):
    def test_form_with_member_account(self):
        pass

    def test_form_with_vcard(self):
        pass
