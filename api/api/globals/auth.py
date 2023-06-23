from user.models import CustomUser
from driver.models import Driver
from manager.models import Manager

def get_user_obj(**data):
    try:
        user = CustomUser.objects.get(**data)
    except CustomUser.DoesNotExist:
        return None

    return user

def authenticate(user: CustomUser, token: str) -> bool:
    obj = None

    if user.role == 1:
        obj = Manager.objects.get(user=user)
    elif user.role == 2:
        obj = Driver.objects.get(user=user)

    if not obj:
        return False

    if obj.token != token:
        return False

    return True