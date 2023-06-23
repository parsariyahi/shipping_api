from rest_framework.serializers import ModelSerializer

from .models import Carry

class DriverSerializer(ModelSerializer):

    class Meta:
        model = Carry
        fields = ("__all__")