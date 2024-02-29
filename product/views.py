from django.shortcuts import render
from rest_framework import viewsets
from product.serializers import ProductSerializer
from product.models import Product
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import ProductFilter

# Create your views here.
class CatalogViewSet(viewsets.ModelViewSet):
    filter_backends = (OrderingFilter,)
    ordering_fields = ['price'] 
    filterset_fields = ['price']
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
