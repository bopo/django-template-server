from django.core.urlresolvers import reverse
from rest_framework.test import APITestCase


class VersionAPIViewTestCase(APITestCase):
    url = reverse("v1.0:version-list")

    def test_version_connected(self):
        response = self.client.get(self.url)
        self.assertEqual(200, response.status_code)
