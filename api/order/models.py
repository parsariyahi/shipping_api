from django.db import models
from manager.models import Manager

class Order(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.RESTRICT)
    title = models.CharField(max_length=250)
    source = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)