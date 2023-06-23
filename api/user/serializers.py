from rest_framework.serializers import ModelSerializer, ValidationError

from .models import CustomUser

from driver.models import Driver
from manager.models import Manager

class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("username", "password", "role")

    def save(self, **kwargs):

        user = super().save(**kwargs)

        role = user.role
        if role == 1:
            uesr_type_obj = Manager.objects.create(user=user, token="some")
        elif role == 2:
            uesr_type_obj = Driver.objects.create(user=user, token="some")
        uesr_type_obj.save()

        return user