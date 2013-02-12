from django.test import TestCase

from yaproject.vcard.models import VCard, RequestStore


class VcardModelsTest(TestCase):
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


class AdminTest(TestCase):
    def test_admin_with_vcard(self):
        self.resp = self.client.get('/admin/')
        self.assertEqual(self.resp.status_code, 200)


class VcardViewsTest(TestCase):
    def test_views_with_contacts(self):
        self.resp = self.client.get('/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertTrue(self.resp.context['contacts'])
        self.vcard = self.resp.context['contacts']
        self.assertTrue(self.vcard.name)
        self.assertTrue(self.vcard.surname)
        self.assertTrue(self.vcard.birth_date)
        self.assertTrue(self.vcard.bio)
        self.assertTrue(self.vcard.e_mail)


class RequestStoreTest(TestCase):
    def test_middleware_with_store(self):
        while RequestStore.objects.all().count() != 10:
            self.resp = self.client.get('/')
        self.resp = self.client.get('/request_store/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertEqual(len(self.resp.context['requests']), 10)
        self.req_store = RequestStore.objects.latest('id')
        self.assertNotIn(self.req_store, self.resp.context['requests'])
        self.assertTrue(self.req_store)
        self.assertEqual(self.req_store.host, 'testserver')
        self.assertEqual(self.req_store.path, '/request_store/')
        self.assertTrue(self.req_store.date)
