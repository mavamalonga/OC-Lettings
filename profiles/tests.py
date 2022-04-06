# -*- coding: utf-8 -*-
import unittest
from django.test import Client
from django.urls import reverse


class ProfilesTest(unittest.TestCase):
    def test_profiles(self):
        client = Client()
        response = client.get(reverse('profiles_index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Profiles</title>', response.content)

    def test_profile(self):
        client = Client()
        response = client.get(reverse('profile', kwargs={'username': 'alpha'}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>alpha</title>', response.content)


if __name__ == "__main__":
    unittest.main()
