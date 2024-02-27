from django.shortcuts import render
from rest_framework import viewsets
from product.serializers import ProductSerializer
from product.models import Product


# Create your views here.
class CatalogViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
