# -*- coding: utf-8 -*-
import unittest
from django.test import Client
from django.urls import reverse


class HomeTest(unittest.TestCase):

    def test_homepage(self):
        client = Client()
        response = client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Holiday Homes</title>', response.content)


if __name__ == "__main__":
    unittest.main()
