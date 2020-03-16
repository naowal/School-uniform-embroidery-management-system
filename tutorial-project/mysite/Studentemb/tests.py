import unittest
from django.urls import reverse
from django.test import Client
from .models import StudentEmbInfo, user
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_studentembinfo(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["firstname"] = "firstname"
    defaults["lastname"] = "lastname"
    defaults["schoolname"] = "schoolname"
    defaults["moreinfo"] = "moreinfo"
    defaults["status"] = "status"
    defaults["color"] = "color"
    defaults["create_by"] = "create_by"
    defaults["price_baht"] = "price_baht"
    defaults.update(**kwargs)
    return StudentEmbInfo.objects.create(**defaults)


def create_user(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults.update(**kwargs)
    return user.objects.create(**defaults)


class StudentEmbInfoViewTest(unittest.TestCase):
    '''
    Tests for StudentEmbInfo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_studentembinfo(self):
        url = reverse('Studentemb_studentembinfo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_studentembinfo(self):
        url = reverse('Studentemb_studentembinfo_create')
        data = {
            "name": "name",
            "firstname": "firstname",
            "lastname": "lastname",
            "schoolname": "schoolname",
            "moreinfo": "moreinfo",
            "status": "status",
            "color": "color",
            "create_by": "create_by",
            "price_baht": "price_baht",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_studentembinfo(self):
        studentembinfo = create_studentembinfo()
        url = reverse('Studentemb_studentembinfo_detail', args=[studentembinfo.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_studentembinfo(self):
        studentembinfo = create_studentembinfo()
        data = {
            "name": "name",
            "firstname": "firstname",
            "lastname": "lastname",
            "schoolname": "schoolname",
            "moreinfo": "moreinfo",
            "status": "status",
            "color": "color",
            "create_by": "create_by",
            "price_baht": "price_baht",
        }
        url = reverse('Studentemb_studentembinfo_update', args=[studentembinfo.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class userViewTest(unittest.TestCase):
    '''
    Tests for user
    '''
    def setUp(self):
        self.client = Client()

    def test_list_user(self):
        url = reverse('Studentemb_user_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_user(self):
        url = reverse('Studentemb_user_create')
        data = {
            "name": "name",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_user(self):
        user = create_user()
        url = reverse('Studentemb_user_detail', args=[user.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_user(self):
        user = create_user()
        data = {
            "name": "name",
        }
        url = reverse('Studentemb_user_update', args=[user.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


