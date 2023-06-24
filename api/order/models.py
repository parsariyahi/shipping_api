from django.db import models
from manager.models import Manager

class Order(models.Model):
    manager = models.ForeignKey(Manager, on_delete=models.RESTRICT)
    title = models.CharField(max_length=250)
    src_lat = models.IntegerField()
    src_long = models.IntegerField()
    dest_lat = models.IntegerField()
    dest_long = models.IntegerField()
    status = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)