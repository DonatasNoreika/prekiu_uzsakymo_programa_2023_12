from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Status(models.Model):
    name = models.CharField(verbose_name="Pavadinimas", max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(verbose_name="Pavadinimas", max_length=100)
    price = models.FloatField(verbose_name="Kaina")

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(to=User, verbose_name="Vartotojas", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Data", auto_now_add=True)
    status = models.ForeignKey(to="Status", verbose_name="Būsena", on_delete=models.SET_NULL, null=True, blank=True)

    def total(self):
        total = 0
        lines = self.lines.all()
        for line in lines:
            total += line.suma()
        return total

    def __str__(self):
        return str(self.date)

class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", verbose_name="Užsakymas", on_delete=models.CASCADE, related_name="lines")
    product = models.ForeignKey(to="Product", verbose_name="Prekė", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(verbose_name="Kiekis")

    def suma(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.order} ({self.product} - {self.quantity})"