from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

User = get_user_model()

class AuthenticationTestCase(TestCase):
    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(email='test@example.com', username='testuser', password='password123')

    def test_authentication(self):
        # Test valid credentials
        user = authenticate(email='test@example.com', password='password123')
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'test@example.com')

        # Test invalid credentials
        user_invalid = authenticate(email='test@example.com', password='wrongpassword')
        self.assertIsNone(user_invalid)

        user_not_exist = authenticate(email='nonexistent@example.com', password='password123')
        self.assertIsNone(user_not_exist)
