from rest_framework import serializers
from .models import TaskEntity

class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    due_date = serializers.DateTimeField()
    completed = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return TaskEntity(**validated_data)