from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

"""
The Token field is not standard and secure,
best practice is JWT and Oauth2,
but I do not have time to code a good auth system,
so i handle it with simple token thing.
"""

class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT)
    token = models.CharField(max_length=250)