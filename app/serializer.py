from rest_framework import serializers
from .models import Category, Products, Review


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()
    category = serializers.CharField()


class ReviewSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    product = serializers.CharField()
