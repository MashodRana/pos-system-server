from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from sale.models import Sale
from sale.serializers import SaleSerializer


# Create your views here.
class SaleView(APIView):
    def get(self, request, format=None):
        sales = Sale.objects.all()
        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            sale = serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class SaleDetailView(APIView):
    def get(self, request, id, format=None):
        sale = get_object_or_404(Sale, pk=id)
        serializer = SaleSerializer(sale)
        return Response(serializer.data, status=HTTP_200_OK)
