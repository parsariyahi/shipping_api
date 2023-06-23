from django.db import models
from django.contrib.auth.models import AbstractUser

ROLES = [
    (0, "Basic"),
    (1, "Manger"),
    (2, "Driver"),
]

class CustomUser(AbstractUser):
    role = models.IntegerField(choices=ROLES, default=0)
