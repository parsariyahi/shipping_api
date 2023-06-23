from django.db import models
from order.models import Order
from driver.models import Driver

class Carry(models.Model):
    order = models.OneToOneField(Order, on_delete=models.RESTRICT)
    driver = models.ForeignKey(Driver, on_delete=models.RESTRICT)
    carry_at = models.DateTimeField(auto_now=True)
    delivered = models.BooleanField(default=False)
    delivered_at = models.DateTimeField(null=True, blank=True)