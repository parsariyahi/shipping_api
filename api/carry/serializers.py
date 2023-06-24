from rest_framework.serializers import ModelSerializer

from .models import Carry

class CarrySerializer(ModelSerializer):

    class Meta:
        model = Carry
        fields = ("__all__")