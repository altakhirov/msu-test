from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView

from tasks.models import Task
from tasks.permissions import IsCreator
from tasks.serializers import TaskSerializer


class TaskListAPI(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class UserTaskListAPI(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(created_by=self.request.user)


class TaskCreateAPI(CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskUpdateAPI(UpdateAPIView):
    permission_classes = [IsCreator]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDeleteAPI(DestroyAPIView):
    permission_classes = [IsCreator]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
