from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


class LoginTestCase(TestCase):
    PASSWORD = 'testpassword'

    def setUp(self):
        self.user = User.objects.create_user(
            'test', 'test@test.com', self.PASSWORD)

    def test_standard_login(self):
        """
        Standard login is disabled in favor of oauth
        """
        user = authenticate(username='test', password=self.PASSWORD)
        self.assertTrue(user is None)
