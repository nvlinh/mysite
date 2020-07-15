from django.test import TestCase
from django.test import Client
from unittest.mock import MagicMock
from researchUT.models import ChoiceMock


class LoginTest(TestCase):
    def test_Login(self):
        c = Client()
        response = c.post('/admin/login/', {'username': 'lieu@paradox.ai', 'password': '13456'})
        self.assertEqual(response.status_code, 200)
        print(response.content)
