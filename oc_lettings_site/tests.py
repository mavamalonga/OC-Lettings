# -*- coding: utf-8 -*-
from django.test import TestCase


class URLTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Holiday Homes', response.content)


# py manage.py test
