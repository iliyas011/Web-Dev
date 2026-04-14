from rest_framework import serializers
from .models import Category, Product


class Brief(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'