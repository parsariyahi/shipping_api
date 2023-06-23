from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    token = models.CharField(max_length=250)