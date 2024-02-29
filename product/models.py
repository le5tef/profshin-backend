from django.db import models
from django.core.files import File
import django_filters
from django_filters import RangeFilter, NumberFilter,CharFilter
from io import BytesIO
from PIL import Image


class Category(models.Model):
    name = models.CharField(max_length=255, verbose_name='Категория')

    class Meta:
        ordering = ('name',)
        verbose_name='Категория'
        verbose_name_plural='Категории'

    def __str__(self):
        return self.name


class Property(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    unit = models.CharField(max_length=255, blank=True, verbose_name='Единица измерения')

    class Meta:
        ordering = ('name',)
        verbose_name='Характеристика'
        verbose_name_plural='Характеристики'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    price = models.IntegerField(verbose_name='Цена')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        verbose_name='Товар'
        verbose_name_plural='Товары'

    def __str__(self):
        return self.name


class ProductProperty(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, verbose_name='Характеристика')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Товар')
    value = models.JSONField(max_length=255, verbose_name='Значение')

    class Meta:
        ordering = ('property',)
        verbose_name='Характеристика товара'
        verbose_name_plural='Характеристики товара'

    def __str__(self):
        return f'{self.property} {self.value}'

class ProductFilter(django_filters.FilterSet):
    price = RangeFilter()
    diametr = NumberFilter()
    height = NumberFilter()
    width = NumberFilter()
    manufacturer = CharFilter()
    class Meta: 
        model = Product
        fields = ['price']