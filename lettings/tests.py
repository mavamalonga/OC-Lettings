# -*- coding: utf-8 -*-
import unittest
from django.test import Client
from django.urls import reverse


class LettingsTest(unittest.TestCase):
    def test_lettings(self):
        client = Client()
        response = client.get(reverse('lettings'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Lettings</title>', response.content)

    def test_letting(self):
        client = Client()
        response = client.get('/lettings/1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Joshua Tree Green Haus /w Hot Tub</title>', response.content)


if __name__ == "__main__":
    unittest.main()
