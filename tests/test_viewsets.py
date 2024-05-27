#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the `drf-rw-serializers` viewsets module.
"""

from __future__ import absolute_import, unicode_literals

from django.urls import reverse

from model_bakery import baker

from example_app.serializers import OrderCreateSerializer, OrderListSerializer
from test_utils.base_tests import (
    BaseTestCase,
    TestCreateRequestSuccess,
    TestListRequestSuccess,
    TestRetrieveRequestSuccess,
    TestUpdateRequestSuccess,
)


class OrderViewsetListCreateTests(BaseTestCase, TestListRequestSuccess, TestCreateRequestSuccess):
    def setUp(self):
        super().setUp()
        self.view_url = reverse("viewset_list_create")
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderViewsetRetrieveUpdateDestroyTests(
    BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess
):
    def setUp(self):
        super().setUp()
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("viewset_retrieve_update_destroy", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer
