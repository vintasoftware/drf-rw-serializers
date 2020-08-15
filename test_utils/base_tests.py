from django.contrib.auth import get_user_model
from model_bakery import baker
from rest_framework.test import APITestCase, APIClient

from example_app.models import Order
from example_app.serializers import OrderedMealDetailsSerializer


class BaseTestCase(APITestCase):

    def setUp(self):
        self.meals = baker.make('example_app.Meal', _quantity=3)

        user_model = get_user_model()

        self.user_email = 'user'
        self.user_password = 'the_password'
        self.user = user_model.objects.create_user(
            username=self.user_email, password=self.user_password)

        self.auth_client = APIClient()
        self.auth_client.force_authenticate(self.user)


class TestListRequestSuccess(object):

    def test_list_request_success(self):
        orders = baker.make('example_app.Order', _quantity=3)
        for order in orders:
            baker.make('example_app.OrderedMeal', order=order, _quantity=2)

        response = self.auth_client.get(self.view_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.data, self.list_serializer_class(orders, many=True).data)


class TestRetrieveRequestSuccess(object):

    def test_list_request_success(self):
        order = baker.make('example_app.Order')
        baker.make('example_app.OrderedMeal', order=order, _quantity=2)
        response = self.auth_client.get(self.view_url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertCountEqual(
            response.data, self.retrieve_serializer_class(order).data)


class TestCreateRequestSuccess(object):

    def test_create_request_success(self):
        data = {
            'table_number': 100,
            'ordered_meals': [
                {
                    'quantity': 1,
                    'meal': self.meals[0].id,
                },
                {
                    'quantity': 2,
                    'meal': self.meals[1].id,
                },
            ],
        }
        response = self.auth_client.post(self.view_url, data, format='json')
        self.assertEqual(response.status_code, 201)
        order = Order.objects.get(id=response.data['id'])
        self.assertEqual(response.data, self.create_out_serializer_class(order).data)
        self.assertEqual(order.table_number, data['table_number'])

        for ordered_meal_dict in data['ordered_meals']:
            ordered_meal = order.ordered_meals.filter(meal__id=ordered_meal_dict['meal']).first()
            self.assertIsNotNone(ordered_meal)
            self.assertEqual(ordered_meal.quantity, ordered_meal_dict['quantity'])


class TestUpdateRequestSuccess(object):

    def test_update_request_success(self):
        data = {
            'table_number': 2,
            'ordered_meals': [
                {
                    'quantity': 10,
                    'meal': self.meals[0].id,
                },
                {
                    'quantity': 20,
                    'meal': self.meals[1].id,
                },
            ]
        }
        response = self.auth_client.put(self.view_url, data, format='json')
        self.object.refresh_from_db()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.update_out_serializer_class(self.object).data)
        self.assertEqual(self.object.table_number, data['table_number'])

        for ordered_meal_dict in data['ordered_meals']:
            ordered_meal = self.object.ordered_meals.filter(
                meal__id=ordered_meal_dict['meal']).first()
            self.assertIsNotNone(ordered_meal)
            self.assertEqual(ordered_meal.quantity, ordered_meal_dict['quantity'])

    def test_partial_update_table_number_request_success(self):
        old_ordered_meals = OrderedMealDetailsSerializer(
            self.object.ordered_meals.all(), many=True).data

        data = {
            'table_number': 2,
        }

        response = self.auth_client.patch(self.view_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.object.refresh_from_db()
        self.assertEqual(response.data, self.update_out_serializer_class(self.object).data)
        self.assertEqual(self.object.table_number, data['table_number'])
        self.assertCountEqual(
            OrderedMealDetailsSerializer(self.object.ordered_meals.all(), many=True).data,
            old_ordered_meals)

    def test_partial_update_ordered_meals_request_success(self):
        old_table_number = self.object.table_number
        data = {
            'ordered_meals': [
                {
                    'quantity': 10,
                    'meal': self.meals[2].id,
                },
            ]
        }
        response = self.auth_client.patch(self.view_url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.object.refresh_from_db()
        self.assertEqual(response.data, self.update_out_serializer_class(self.object).data)
        for ordered_meal_dict in data['ordered_meals']:
            ordered_meal = self.object.ordered_meals.filter(
                meal__id=ordered_meal_dict['meal']).first()
            self.assertIsNotNone(ordered_meal)
            self.assertEqual(ordered_meal.quantity, ordered_meal_dict['quantity'])
        self.assertEqual(self.object.table_number, old_table_number)
