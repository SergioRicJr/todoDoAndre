from rest_framework import serializers
from .models import TaskEntity


class TaskSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    description = serializers.CharField()
    due_date = serializers.DateTimeField()
    completed = serializers.BooleanField(default=False)
    user_id = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return TaskEntity(**validated_data)


class TaskUpdateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False)
    due_date = serializers.DateTimeField(required=False)
    completed = serializers.BooleanField(required=False)

    # def create(self, validated_data):
    #     return TaskEntity(**validated_data)
