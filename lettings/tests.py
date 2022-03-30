# -*- coding: utf-8 -*-
import unittest
from django.test import Client


class LettingsTest(unittest.TestCase):
    def test_lettings(self):
        client = Client()
        response = client.get('/lettings/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Joshua Tree Green Haus', response.content)

    def test_letting(self):
        client = Client()
        response = client.get('/lettings/1/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<p>7217 Bedford Street</p>', response.content)


if __name__ == "__main__":
    unittest.main()
