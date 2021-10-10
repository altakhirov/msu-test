from django.urls import path

from tasks.views import *

app_name = 'tasks'


urlpatterns = [
    path('list', TaskListAPI.as_view()),
    path('list/created-by-me', UserTaskListAPI.as_view()),
    path('create', TaskCreateAPI.as_view()),
    path('update/<int:pk>', TaskUpdateAPI.as_view()),
    path('delete/<int:pk>', TaskDeleteAPI.as_view()),
]
