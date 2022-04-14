from rest_framework import serializers
from .models import Name_task

class taskSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    class Meta:
        model=Name_task
        fields=('__all__')