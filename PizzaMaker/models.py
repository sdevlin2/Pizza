from django.db import models

class Topping(models.Model):
    topping_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topping_name


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    pizza_toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.pizza_name