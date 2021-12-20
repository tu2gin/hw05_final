from django.conf import settings
from django.test import Client, TestCase


class StaticURLHomepageTests(TestCase):

    def setUp(self):
        self.guest_client = Client()

    def test_techpage(self):
        response = self.guest_client.get('/about/tech/')
        self.assertEqual(response.status_code, settings.OK)

    def test_authorpage(self):
        response = self.guest_client.get('/about/author/')
        self.assertEqual(response.status_code, settings.OK)
