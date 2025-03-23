from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class AuthenticationTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_authenticated_access(self):
        response = self.client.get("/your-api-endpoint/")
        self.assertEqual(response.status_code, 200)

    def test_unauthenticated_access(self):
        self.client.credentials()  # Remove token
        response = self.client.get("/your-api-endpoint/")
        self.assertEqual(response.status_code, 401)
