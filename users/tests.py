from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase

User = get_user_model()


class UserSignupTestCase(APITestCase):

    def test_signup(self):
        payload = {
            'username': 'some_username',
            'password': '24kf9jg9esjg032g',
            'first_name': 'Patrick',
            'last_name': 'Kane'
        }
        response = self.client.post('/user/signup', data=payload)
        self.assertEqual(response.status_code, 201)


class UserAuthTestCase(APITestCase):
    username = 'my_username'
    password = '24kf9jg9esjg032g'

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            first_name='Patrick',
            last_name='Kane'
        )

    def test_token_receive(self):
        response = self.client.post(
            '/user/token',
            {
                'username': self.username,
                'password': self.password
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_token_refresh(self):
        response = self.client.post(
            '/user/token',
            {
                'username': self.username,
                'password': self.password
            },
            format='json'
        )
        refresh_token = response.data.get('refresh')
        response_to_refresh = self.client.post(
            '/user/token/refresh',
            {
                'username': self.username,
                'password': self.password,
                'refresh': refresh_token
            },
            format='json'
        )
        self.assertEqual(response_to_refresh.status_code, 200)
