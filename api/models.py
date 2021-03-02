from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Storage(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    storage = models.ManyToManyField(Storage)
    store = models.ManyToManyField(Store)
    product_in_storage = models.IntegerField(default=0)
    product_in_store = models.IntegerField(default=0)
    sales_product_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name


