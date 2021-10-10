from django.contrib.auth import get_user_model

from rest_framework.test import APITestCase, APIClient

from tasks.models import Task

User = get_user_model()


class TaskTestCase(APITestCase):
    username = 'my_username'
    password = '24kf9jg9esjg032g'

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            first_name='Patrick',
            last_name='Kane'
        )
        self.user_2 = User.objects.create_user(
            username='my_username_2',
            password='t3tf9fwa3t3t3',
            first_name='Cale',
            last_name='Makar'
        )
        self.task = Task.objects.create(
            created_by=self.user,
            title='Created test task',
            description='Description goes here',
            deadline='2021-11-11',
        )
        self.task.responsibles.add(self.user)
        self.task_2 = Task.objects.create(
            created_by=self.user_2,
            title='Created test task no 2',
            description='Description goes here',
            deadline='2021-11-19',
        )
        self.task_2.responsibles.add(self.user)
        response = self.client.post(
            '/user/token',
            {
                'username': self.username,
                'password': self.password
            },
            format='json'
        )
        self.access_token = response.data.get('access')

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

    def test_task_list(self):
        response = self.client.get('/task/list')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Task.objects.all().count(), 2)

    def test_user_task_list(self):
        response = self.client.get('/task/list/created-by-me')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_task_create(self):
        response = self.client.post(
            '/task/create',
            {
                'title': 'Task to perform',
                'description': 'Description for task here',
                'deadline': '2021-12-12',
                'responsibles': [self.user.pk]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 201)

    def test_task_update(self):
        response = self.client.put(
            f'/task/update/{self.task.pk}',
            {
                'title': 'Task to perform updated',
                'description': 'Description for task here',
                'deadline': '2021-12-22',
                'responsibles': [self.user.pk, self.user_2.pk]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 200)

    def test_prohibited_task_update(self):
        response = self.client.put(
            f'/task/update/{self.task_2.pk}',
            {
                'title': 'Task to perform updated',
                'description': 'Description for task here',
                'deadline': '2021-12-22',
                'responsibles': [self.user.pk]
            },
            format='json'
        )
        self.assertEqual(response.status_code, 403)

    def test_task_delete(self):
        response = self.client.delete(f'/task/delete/{self.task.pk}')
        self.assertEqual(response.status_code, 204)

    def test_prohibited_task_delete(self):
        response = self.client.delete(f'/task/delete/{self.task_2.pk}')
        self.assertEqual(response.status_code, 403)
