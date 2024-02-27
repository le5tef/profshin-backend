from product.models import Product, ProductProperty, Property, Category
from rest_framework import serializers


class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = ['id', 'name', 'unit']


class ProductPropertySerializer(serializers.ModelSerializer):
    property = PropertySerializer()

    class Meta:
        model = ProductProperty
        fields = ['id', 'property', 'value']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    properties = ProductPropertySerializer(many=True, source='productproperty_set')
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = '__all__'
