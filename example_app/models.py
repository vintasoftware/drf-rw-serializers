# -*- coding: utf-8 -*-

from django.db import models


class Order(models.Model):
    table_number = models.IntegerField()

    @property
    def total_price(self):
        return sum(
            [o.meal.price * o.quantity for o in self.ordered_meals.select_related("meal").all()]
        )


class OrderedMeal(models.Model):
    order = models.ForeignKey("Order", related_name="ordered_meals", on_delete=models.CASCADE)
    meal = models.ForeignKey("Meal", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


class Meal(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=5)
