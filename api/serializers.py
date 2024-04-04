from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField()
    completed = serializers.BooleanField()
    description = serializers.CharField()
    created_at = serializers.DateTimeField()