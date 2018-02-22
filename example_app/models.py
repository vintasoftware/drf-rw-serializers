# -*- coding: utf-8 -*-

from django.db import models


class Order(models.Model):
    table_number = models.IntegerField()

    @property
    def total_price(self):
        orderedself.ordered_meals.all()

class OrderedMeal(models.Model):
    order = models.ForeignKey('Order', related_name="ordered_meals")
    meal = models.ForeignKey('Meal')
    quantity = models.IntegerField(default=1)


class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)