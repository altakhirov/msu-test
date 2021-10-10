from rest_framework import serializers

from tasks.models import Task
from users.models import User


class ResponsibleSerializer(serializers.PrimaryKeyRelatedField):

    def to_representation(self, instance):
        return instance.username

    class Meta:
        model = User


class TaskSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    file = serializers.FileField(max_length=None, allow_empty_file=True, allow_null=True, required=False)
    responsibles = ResponsibleSerializer(many=True, queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['created_by', 'title', 'description', 'deadline', 'file', 'responsibles']

    def update(self, instance, validated_data):
        data = validated_data.copy()
        if not data.get('file'):
            if instance.file:
                instance.file.delete()
        return super().update(instance, data)
