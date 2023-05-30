from rest_framework.serializers import ModelSerializer

from sale.models import Sale


class SaleSerializer(ModelSerializer):
    class Meta:
        model = Sale
        fields = "__all__"

