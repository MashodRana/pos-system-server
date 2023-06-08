from rest_framework import serializers

from stock.models import Stock


class StockSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', required=False)
    sku = serializers.CharField(source='product.pk', required=False)
    unit = serializers.CharField(source='product.unit.short_form', required=False)


    class Meta:
        model = Stock
        fields = '__all__'
