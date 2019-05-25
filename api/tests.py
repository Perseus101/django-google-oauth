from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from api.models import Profile


class LoginTestCase(TestCase):
    PASSWORD = 'testpassword'
    ABOUT = 'Test'

    def setUp(self):
        self.user = User.objects.create_user(
            'test', 'test@test.com', self.PASSWORD)
        self.profile = Profile(user=self.user, about=self.ABOUT)

    def test_profile(self):
        """
        Standard login is disabled in favor of oauth
        """
        self.assertTrue(self.user is not None)
        self.assertEquals(self.profile.about, self.ABOUT)
