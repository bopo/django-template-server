import json

from ddt import ddt, data, unpack
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

TEST_DATA = ("python", "selenium", "unittest", "sd", "sdfadf", "sdfasdfadfa", "sdfasdfad")


@ddt
class UserLoginTestCase(APITestCase):
    url = reverse("rest_login")
    username = None
    password = None
    email = None
    user = None

    def setUp(self):
        self.username = "18742514206"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)

    @data(*TEST_DATA)
    def test_without_password(self, keyword):
        response = self.client.post(self.url, {"username": keyword})
        self.assertEqual(400, response.status_code)

    @data(*TEST_DATA)
    def test_with_wrong_password(self, password):
        response = self.client.post(self.url, {"username": self.username, "password": password})
        self.assertEqual(400, response.status_code)

    @data(['18742514206', 'you_know_nothing'])
    @unpack
    def test_with_valid_data(self, username, password):
        response = self.client.post(self.url, {"username": username, "password": password})
        self.assertEqual(200, response.status_code)
        self.assertTrue("key" in json.loads(response.content))

    @unpack
    def tearDown(self):
        pass


@ddt
class UserVerifyTestCase(APITestCase):
    url = reverse("rest_verify_mobile")
    username = None

    def setUp(self):
        self.username = "18742514206"

    def test_verify_without_username(self):
        response = self.client.post(self.url, {})
        self.assertEqual(400, response.status_code)

    @data(*TEST_DATA)
    def test_verify_without_valid_mobile(self, username):
        response = self.client.post(self.url, {"username": username})
        self.assertEqual(400, response.status_code)

    def test_verify_with_valid_data(self):
        response = self.client.post(self.url, {"username": self.username})
        self.assertEqual(200, response.status_code)


class UserRegisterTestCase(APITestCase):
    url = reverse("rest_register")
    username = None
    password = None
    email = None
    user = None

    def setUp(self):
        self.username = "18742514206"
        self.password = "you_know_nothing"

    def test_register_without_password(self):
        response = self.client.post(self.url, {"username": "snowman"})
        self.assertEqual(400, response.status_code)

    def test_register_without_valid_mobile(self):
        response = self.client.post(self.url, {"username": "snowman", "password": "I_know"})
        self.assertEqual(400, response.status_code)

    def test_register_with_wrong_password(self):
        response = self.client.post(self.url, {"username": self.username, "password": "I_know"})
        self.assertEqual(400, response.status_code)

    def test_register_with_valid_data(self):
        response = self.client.post(self.url, {"username": self.username, "password": self.password, "verify": '1111'})
        self.assertEqual(201, response.status_code)
        self.assertTrue("key" in json.loads(response.content))


class UserLogoutTestCase(APITestCase):
    url = reverse("rest_logout")
    username = None
    password = None
    email = None
    token = None
    user = None

    def setUp(self):
        self.username = "18742514206"
        self.email = "john@snow.com"
        self.password = "you_know_nothing"
        self.user = User.objects.create_user(self.username, self.email, self.password)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_logout(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
        self.assertFalse(Token.objects.filter(key=self.token).exists())
