from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .models import Category, Products, Review
from .serializer import CategorySerializer, ProductSerializer, ReviewSerializer


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer


class CategoryRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ReviewRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



