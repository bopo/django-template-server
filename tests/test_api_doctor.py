# -*- coding: utf-8 -*-

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
