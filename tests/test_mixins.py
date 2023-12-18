#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the `drf-rw-serializers` mixins module.
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


class OrderCreateWithMixinEndpointTests(BaseTestCase, TestCreateRequestSuccess):

    def setUp(self):
        super(OrderCreateWithMixinEndpointTests, self).setUp()
        self.view_url = reverse('create_mixin')
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderUpdateWithMixinEndpointTests(BaseTestCase, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderUpdateWithMixinEndpointTests, self).setUp()
        self.object = baker.make('example_app.Order')
        baker.make('example_app.OrderedMeal', order=self.object, _quantity=2)
        self.view_url = reverse('update_mixin', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithMixinEndpointTests(BaseTestCase, TestListRequestSuccess):

    def setUp(self):
        super(OrderListWithMixinEndpointTests, self).setUp()
        self.view_url = reverse('list_mixin')
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveWithMixinEndpointTests(BaseTestCase, TestRetrieveRequestSuccess):

    def setUp(self):
        super(OrderRetrieveWithMixinEndpointTests, self).setUp()
        self.object = baker.make('example_app.Order')
        baker.make('example_app.OrderedMeal', order=self.object, _quantity=2)
        self.view_url = reverse('retrieve_mixin', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
