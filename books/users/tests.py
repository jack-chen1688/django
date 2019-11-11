from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse, resolve

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'user1',
            email = 'user1@email.com',
            password = 'testpass123'
        )

        self.assertEqual(user.username, 'user1' )
        self.assertEqual(user.email, 'user1@email.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'adminuser',
            email = 'adminuser@email.com',
            password = 'testpass123'
        )

        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.email, 'adminuser@email.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

class SignupTests(TestCase):

    username = 'newuser'
    email = 'newuser@email.com'

    def setUp(self):
        url = reverse('account_signup')
        self.response = self.client.get(url)

    def test_signup_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed(self.response, 'account/signup.html')
        self.assertContains(self.response, "Sign Up")
        self.assertNotContains(self.response, "Hi there!")

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(self.username, self.email)
        print(f"hello, number of users is {get_user_model().objects.all().count()}")
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
        

