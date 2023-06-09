from django.db import models

from common.models import TimeStamp


# Create your models here.
class Sale(TimeStamp):
    details = models.TextField()
    total_price = models.FloatField()
    customer = models.CharField(max_length=255)
    paid_amount = models.FloatField()
    due_amount = models.FloatField()

    def __str__(self):
        return f"Order-{self.id}"
