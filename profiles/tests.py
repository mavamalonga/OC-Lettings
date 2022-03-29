# -*- coding: utf-8 -*-
import unittest
from django.test import Client

class ProfilesTest(unittest.TestCase):
    def test_profiles(self):
        client = Client()
        response = client.get('/profiles/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<h1>Profiles</h1>', response.content)

    def test_profile(self):
        client = Client()
        response = client.get('/profiles/alpha/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>Email: alpha@exemple.com</p>', response.content)
