from django.test import TestCase

from application_user.models import ApplicationUser


# Create your tests here.

class TestTheTest(TestCase):
    def test_should_return_true(self):
        assert True is True


class TestApplicationUser(TestCase):
    def test_should_create_user(self):
        ApplicationUser.objects.create(
            user_name="test",
            user_email="test@yahoo.com",
            user_password="test1234",
            user_type="test"
        )

        test_user = ApplicationUser.objects.filter(user_name="test").first()

        self.assertEqual(test_user.user_name, "test")
        self.assertEqual(test_user.user_email, "test@yahoo.com")
        self.assertEqual(test_user.user_password, "test1234")
        self.assertEqual(test_user.user_type, "test")
