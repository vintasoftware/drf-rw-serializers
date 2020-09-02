#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the `drf-rw-serializers` viewsets module.
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


class OrderViewsetListCreateTests(
        BaseTestCase, TestListRequestSuccess, TestCreateRequestSuccess):

    def setUp(self):
        super(OrderViewsetListCreateTests, self).setUp()
        self.view_url = reverse('viewset_list_create')
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderViewsetRetrieveUpdateDestroyTests(
        BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderViewsetRetrieveUpdateDestroyTests, self).setUp()
        self.object = baker.make('example_app.Order')
        baker.make('example_app.OrderedMeal', order=self.object, _quantity=2)
        self.view_url = reverse(
            'viewset_retrieve_update_destroy', kwargs={'pk': self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer
