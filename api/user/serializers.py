from rest_framework.serializers import ModelSerializer, ValidationError

from .models import CustomUser

from driver.models import Driver
from manager.models import Manager
from api.globals import generate_token

class UserSerializer(ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("username", "password", "role")

    def save(self, **kwargs):

        user = super().save(**kwargs)

        role = user.role
        token = generate_token(user.username, user.password)

        data = {
            "user": user,
            "token": token,
        }

        if role == 1:
            uesr_type_obj = Manager.objects.create(**data)
        elif role == 2:
            uesr_type_obj = Driver.objects.create(**data)
        uesr_type_obj.save()

        return user