<<<<<<< HEAD
from django.test import TestCase
=======
from django.utils import unittest
from django.test import Client
from django.template import RequestContext
from django.test.client import RequestFactory
from django.conf import settings as django_settings
from django.contrib.auth.models import User
from yaproject.vcard.context_processor import add_settings
from django.contrib.auth.forms import AuthenticationForm
>>>>>>> master

from yaproject.vcard.models import VCard, RequestStore
from yaproject.vcard.forms import MemberAccountForm


<<<<<<< HEAD
class VcardModelsTest(TestCase):
    def test_vcard_with_data(self):
=======
class BaseTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        self.user_data = {
            'username': 'test',
            'email': 'test@test.com',
            'password': '1'
        }
>>>>>>> master
        self.vcard = VCard.objects.get(pk=1)


class VcardModelsTest(BaseTest):
    def test_vcard_with_data(self):
        self.assertTrue(self.vcard.name)
        self.assertTrue(self.vcard.surname)
        self.assertTrue(self.vcard.birth_date)
        self.assertTrue(self.vcard.bio)
        self.assertTrue(self.vcard.e_mail)

    def test_vcard_with_unicode(self):
<<<<<<< HEAD
        self.vcard = VCard.objects.get(pk=1)
        self.assertEqual('Yaroslav Tsarevsky', self.vcard.__unicode__())


class AdminTest(TestCase):
    def test_admin_with_vcard(self):
        self.resp = self.client.get('/admin/')
        self.assertEqual(self.resp.status_code, 200)


class VcardViewsTest(TestCase):
=======
        self.assertEqual('Yaroslav Tsarevsky', self.vcard.__unicode__())


class AdminTest(BaseTest):
    def test_admin_with_vcard(self):
        self.resp = self.client.get('/admin/vcard/vcard/')
        self.assertEqual(self.resp.status_code, 200)


class VcardViewsTest(BaseTest):
>>>>>>> master
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
<<<<<<< HEAD
=======

    def test_views_with_login(self):
        User.objects.create_user(**self.user_data)
        self.resp = self.client.get('/login/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertIsInstance(self.resp.context['form'], AuthenticationForm)
        self.resp = self.client.post('/login/', self.user_data, follow=True)
        self.assertIn('http://testserver/edit/',
            dict(self.resp.redirect_chain))
>>>>>>> master

    def test_views_with_edit_page(self):
        self.client.login(username='admin', password='admin')
        self.resp = self.client.get('/edit/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertEqual(self.resp.context['form'].instance, self.vcard)
        self.data = {
            'name': 'test',
            'surname': 'test',
            'birth_date': '1980-10-10',
            'bio': 'test test',
            'e_mail': 'test@test.com',
            'skype': 'test',
            'mob': '1111111',
            'jid': 'test'
        }
        self.resp = self.client.post('/edit/', self.data, follow=True)
        self.assertIn('http://testserver/', dict(self.resp.redirect_chain))
        self.vcard = VCard.objects.get(pk=1)
        self.assertEqual(self.vcard.name, 'test')
        self.assertEqual(self.vcard.surname, 'test')

    def test_views_with_login_incorrect_data(self):
        self.user_data = {
            'username': 'test1',
            'email': 'test@test.com',
            'password': '1'
        }
        User.objects.create_user(**self.user_data)
        self.user_data['password'] = '2'
        self.resp = self.client.post('/login/', self.user_data)
        self.assertEqual(len(self.resp.context['form'].errors), 1)

    def test_views_with_registration_form_clean_email(self):
        self.user_data = {
            'username': 'test3',
            'email': 'test@test.com',
            'password': '1'
        }
        self.resp = self.client.get('/sign-up/member/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertIsInstance(self.resp.context['form'], MemberAccountForm)
        self.resp = self.client.post('/sign-up/member/', self.user_data)
        self.assertEqual(len(self.resp.context['form'].errors), 1)
        self.user_data = {
            'username': 'test4',
            'email': 'test4@test.com',
            'password': '1'
        }
        self.resp = self.client.post('/sign-up/member/',
            self.user_data, follow=True)
        self.assertIn('http://testserver/', dict(self.resp.redirect_chain))

    def test_views_with_logout(self):
        self.client.login(username='test', password='1')
        self.resp = self.client.get('/')
        self.assertEqual(self.resp.context['user'].username, 'test')
        self.resp = self.client.get('/logout/', follow=True)
        self.resp = self.client.get('/')
        self.assertEqual(self.resp.context['user'].username, '')

<<<<<<< HEAD
class RequestStoreTest(TestCase):
    def test_middleware_with_store(self):
        while RequestStore.objects.all().count() != 10:
            self.resp = self.client.get('/')
=======
    def test_views_with_edit_incorrect_data(self):
        self.client.login(username='admin', password='admin')
        self.resp = self.client.get('/edit/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertEqual(self.resp.context['form'].instance, self.vcard)
        self.resp = self.client.post('/edit/', {'name': ''}, follow=True)
        self.assertEqual(self.resp.context['form'].errors['name'][0],
            'This field is required.')
        self.resp = self.client.post('/edit/',
            {'name': 'test', 'birth_date': '1980'}, follow=True)
        self.assertEqual(self.resp.context['form'].errors['birth_date'][0],
            'Enter a valid date.')

    def  test_views_with_edit_data_not_all(self):
        pass


class RequestStoreTest(BaseTest):
    def test_middleware_with_store(self):
>>>>>>> master
        self.resp = self.client.get('/request_store/')
        self.assertEqual(self.resp.status_code, 200)
        self.assertEqual(len(self.resp.context['requests']), 10)
        self.req_store = RequestStore.objects.latest('id')
        self.assertNotIn(self.req_store, self.resp.context['requests'])
        self.assertTrue(self.req_store)
<<<<<<< HEAD
        self.assertEqual(self.req_store.host, 'testserver')
        self.assertEqual(self.req_store.path, '/request_store/')
        self.assertTrue(self.req_store.date)
=======
        self.assertTrue(self.req_store.host)
        self.assertTrue(self.req_store.path)


class ContextProcessorTest(unittest.TestCase):
    def test_context_processor_with_settings(self):
        factory = RequestFactory()
        request = factory.get('/')
        c = RequestContext(request, {'foo': 'bar'}, [add_settings])
        self.assertTrue('settings' in c)
        self.assertEquals(c['settings'], django_settings)
>>>>>>> master
