# -*- coding: utf-8 -*-
import unittest
from django.test import Client


class HomeTest(unittest.TestCase):

    def test_homepage(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome to Holiday Homes', response.content)


if __name__ == "__main__":
    unittest.main()
