from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    adress = models.CharField(max_length=200)
    date_of_registration = models.DateField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    date_of_addition = models.DateField()


class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_order = models.DateField(auto_now_add=True)
