import json
from django.db.models.signals import post_save
from django.dispatch import receiver

from stock.models import Stock
from sale.models import Sale


@receiver(post_save, sender=Sale)
def update_product_stock(sender, instance, created, **kwargs):
    if created:
        sale_details = json.loads(instance.details)
        to_update_stocks = []
        for obj in sale_details:
            stock = Stock.objects.get(id=int(obj["id"]))
            stock.quantity = stock.quantity-obj['saleQuantity']
            to_update_stocks.append(stock)
        Stock.objects.bulk_update(to_update_stocks, ['quantity'])

