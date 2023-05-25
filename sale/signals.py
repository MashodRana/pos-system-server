import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from stock.models import Stock
from sale.models import Sale


@receiver(post_save, sender=Sale)
def update_product_stock(sender, instance, created, **kwargs):
    if created:
        sale_details = json.loads(instance.details)
        aa = []
        for obj in sale_details:
            s = Stock.objects.get(id=int(obj["id"]))
            s.quantity = s.quantity-obj['saleQuantity']
            aa.append(s)
        Stock.objects.bulk_update(aa,['quantity'])

