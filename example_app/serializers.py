# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import Meal, Order, OrderedMeal


class OrderedMealCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedMeal
        fields = ("id", "quantity", "meal")


class OrderCreateSerializer(serializers.ModelSerializer):
    ordered_meals = OrderedMealCreateSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "table_number", "ordered_meals", "total_price")

    def create(self, validated_data):
        ordered_meals_dict_list = validated_data.pop("ordered_meals")
        instance = Order.objects.create(**validated_data)
        for ordered_meal_dict in ordered_meals_dict_list:
            instance.ordered_meals.create(**ordered_meal_dict)

        return instance

    def update(self, instance, validated_data):
        ordered_meals_dict_list = validated_data.pop("ordered_meals", None)

        instance.table_number = validated_data.pop("table_number", instance.table_number)

        instance.save()

        if ordered_meals_dict_list is not None:
            instance.ordered_meals.all().delete()
            for ordered_meal_dict in ordered_meals_dict_list:
                instance.ordered_meals.create(**ordered_meal_dict)

        return instance


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ("id", "name", "price")


class OrderedMealDetailsSerializer(serializers.ModelSerializer):
    meal = MealSerializer()

    class Meta:
        model = OrderedMeal
        fields = ("id", "quantity", "meal")


class OrderListSerializer(serializers.ModelSerializer):
    ordered_meals = OrderedMealDetailsSerializer(many=True)

    class Meta:
        model = Order
        fields = ("id", "table_number", "ordered_meals", "total_price")
