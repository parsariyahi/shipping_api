from rest_framework.serializers import ModelSerializer

from .models import Driver

class DriverSerializer(ModelSerializer):

    class Meta:
        model = Driver
        fields = ("__all__")