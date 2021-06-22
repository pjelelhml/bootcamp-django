from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
# TDD

User = get_user_model


class UserTestCast(TestCase):

    def setUp(self):  # Python's builtin unittest
        user_a = User(username='phml', email='cfe@invalid.com')
        # User.objects.create()
        # User.objects.create_user()
        user_a_pw = 'some_123_password'
        self.user_a_pw = user_a_pw
        user_a.is_staff = True
        user_a.is_superuser = True
        user_a.save()
        user_a.set_password(user_a_pw)
        self.user_a = user_a

    def test_user_exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_user_password(self):
        # user_qs = User.objects.filter(username__iexact="cfe")
        # user_exists = user_qs.exists() and user_qs.count() == 1
        # self.assertTrue(user_exists)
        # user_a = user_qs.first()
        self.assertTrue(self.user_a.check_password(self.user_a_pw))
