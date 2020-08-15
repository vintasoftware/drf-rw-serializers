#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the `drf-rw-serializers` models module.
"""

from __future__ import absolute_import, unicode_literals

from django.utils import version as django_version
from model_bakery import baker

from test_utils.base_tests import (
    BaseTestCase, TestListRequestSuccess, TestRetrieveRequestSuccess,
    TestCreateRequestSuccess, TestUpdateRequestSuccess)
from example_app.serializers import OrderCreateSerializer, OrderListSerializer


if django_version.get_complete_version() < (2, 0, 0):
    from django.core.urlresolvers import reverse  # pylint: disable=no-name-in-module,import-error
else:
    from django.urls import reverse  # pylint: disable=no-name-in-module,import-error


class OrderListCreateEndpointTests(
        BaseTestCase, TestListRequestSuccess, TestCreateRequestSuccess):

    def setUp(self):
        super(OrderListCreateEndpointTests, self).setUp()
        self.view_url = reverse('list_create')
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderRetrieveUpdateDestroyEndpointTests(
        BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderRetrieveUpdateDestroyEndpointTests, self).setUp()
        self.object = baker.make('example_app.Order')
        baker.make('example_app.OrderedMeal', order=self.object, _quantity=2)
        self.view_url = reverse('retrieve_update_destroy', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithoutReadSerializerEndpointTests(
        BaseTestCase, TestListRequestSuccess):

    def setUp(self):
        super(OrderListWithoutReadSerializerEndpointTests, self).setUp()
        self.view_url = reverse('list_without_read_serializer')
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveUpdateEndpointTests(
        BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderRetrieveUpdateEndpointTests, self).setUp()
        self.object = baker.make('example_app.Order')
        baker.make('example_app.OrderedMeal', order=self.object, _quantity=2)
        self.view_url = reverse('retrieve_update', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderCreateWithGenericEndpointTests(BaseTestCase, TestCreateRequestSuccess):

    def setUp(self):
        super(OrderCreateWithGenericEndpointTests, self).setUp()
        self.view_url = reverse('create')
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderUpdateWithGenericEndpointTests(BaseTestCase, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderUpdateWithGenericEndpointTests, self).setUp()
        self.object = baker.make('example_app.Order')
        baker.make('example_app.OrderedMeal', order=self.object, _quantity=2)
        self.view_url = reverse('update', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithGenericEndpointTests(BaseTestCase, TestListRequestSuccess):

    def setUp(self):
        super(OrderListWithGenericEndpointTests, self).setUp()
        self.view_url = reverse('list')
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveWithGenericEndpointTests(BaseTestCase, TestRetrieveRequestSuccess):

    def setUp(self):
        super(OrderRetrieveWithGenericEndpointTests, self).setUp()
        self.object = baker.make('example_app.Order')
        baker.make('example_app.OrderedMeal', order=self.object, _quantity=2)
        self.view_url = reverse('retrieve', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
