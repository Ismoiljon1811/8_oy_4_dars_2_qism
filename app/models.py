from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name
    

class Products(models.Model):
    name = models.CharField(max_length = 100)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField()
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "category")

    def __str__(self) -> str:
        return self.name
    

class Review(models.Model):
    name = models.CharField(max_length = 100)
    review = models.TextField()
    product = models.ForeignKey(Products, on_delete = models.CASCADE, related_name = "products")

    def __str__(self) -> str:
        return self.name