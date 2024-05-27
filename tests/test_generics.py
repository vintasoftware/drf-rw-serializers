#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the `drf-rw-serializers` models module.
"""

from __future__ import absolute_import, unicode_literals

from unittest import mock

from django.urls import reverse

import pytest
from model_bakery import baker

from drf_rw_serializers import generics
from example_app.serializers import (
    OrderCreateSerializer,
    OrderedMealDetailsSerializer,
    OrderListSerializer,
)
from test_utils.base_tests import (
    BaseTestCase,
    TestCreateRequestSuccess,
    TestListRequestSuccess,
    TestRetrieveRequestSuccess,
    TestUpdateRequestSuccess,
)


class GenericAPIViewGetSerializerClassTests(BaseTestCase):
    def setUp(self):
        class NoSerializerView(generics.GenericAPIView):
            pass

        self.NoSerializerView = NoSerializerView

        class FullSerializerView(generics.GenericAPIView):
            serializer_class = OrderedMealDetailsSerializer
            read_serializer_class = OrderListSerializer
            write_serializer_class = OrderCreateSerializer

        self.FullSerializerView = FullSerializerView

        class RWSerializerView(generics.GenericAPIView):
            read_serializer_class = OrderListSerializer
            write_serializer_class = OrderCreateSerializer

        self.RWSerializerView = RWSerializerView

    def test_serializer_class_not_provided(self):
        with pytest.raises(AssertionError) as excinfo:
            self.NoSerializerView().get_serializer_class()

        self.assertEqual(
            str(excinfo.value),
            (
                "'NoSerializerView' should either include one of `serializer_class` "
                "and `read_serializer_class` attribute, or override one of the "
                "`get_serializer_class()`, `get_read_serializer_class()` method."
            ),
        )

    def test_no_request_provided(self):
        # Return serializer_class over read_serializer_class and write_serializer_class
        self.assertEqual(
            self.FullSerializerView().get_serializer_class(), OrderedMealDetailsSerializer
        )

    def test_read_request_method_provided(self):
        read_methods = ["GET", "HEAD", "OPTIONS", "TRACE"]

        # Return read_serializer_class
        for method in read_methods:
            self.RWSerializerView.request = mock.Mock(method=method)
            self.assertEqual(self.RWSerializerView().get_serializer_class(), OrderListSerializer)

        # Return read_serializer_class even if serializer_class is provided
        for method in read_methods:
            self.FullSerializerView.request = mock.Mock(method=method)
            self.assertEqual(self.FullSerializerView().get_serializer_class(), OrderListSerializer)

    def test_write_request_method_provided(self):
        write_methods = ["POST", "PUT", "PATCH", "DELETE"]

        # Return write_serializer_class
        for method in write_methods:
            self.RWSerializerView.request = mock.Mock(method=method)
            self.assertEqual(self.RWSerializerView().get_serializer_class(), OrderCreateSerializer)

        # Return write_serializer_class even if serializer_class is provided
        for method in write_methods:
            self.FullSerializerView.request = mock.Mock(method=method)
            self.assertEqual(
                self.FullSerializerView().get_serializer_class(), OrderCreateSerializer
            )

    def test_non_read_write_request_method_provided(self):
        non_read_write_method = "CONNECT"

        # Return default serializer_class
        self.RWSerializerView.request = mock.Mock(method=non_read_write_method)
        self.assertIsNone(self.RWSerializerView().get_serializer_class())

        # Return default serializer_class even if read/write serializer classes are provided
        self.FullSerializerView.request = mock.Mock(method=non_read_write_method)
        self.assertEqual(
            self.FullSerializerView().get_serializer_class(), OrderedMealDetailsSerializer
        )


class GenericAPIViewGetReadSerializerClassTests(BaseTestCase):
    def test_read_serializer_class_not_provided(self):
        class NoReadSerializerView(generics.GenericAPIView):
            pass

        with mock.patch.object(
            NoReadSerializerView, "_get_serializer_class"
        ) as mock__get_serializer_class:
            NoReadSerializerView().get_read_serializer_class()

        mock__get_serializer_class.assert_called_once()

    def test_read_serializer_class_provided(self):
        class ReadSerializerClassProvided(generics.GenericAPIView):
            read_serializer_class = OrderListSerializer

        self.assertEqual(
            ReadSerializerClassProvided().get_read_serializer_class(),
            OrderListSerializer,
        )


class GenericAPIViewGetWriteSerializerClassTests(BaseTestCase):
    def test_write_serializer_class_not_provided(self):
        class NoWriteSerializerView(generics.GenericAPIView):
            pass

        with mock.patch.object(
            NoWriteSerializerView, "_get_serializer_class"
        ) as mock__get_serializer_class:
            NoWriteSerializerView().get_write_serializer_class()

        mock__get_serializer_class.assert_called_once()

    def test_write_serializer_class_provided(self):
        class WriteSerializerClassProvided(generics.GenericAPIView):
            write_serializer_class = OrderCreateSerializer

        self.assertEqual(
            WriteSerializerClassProvided().get_write_serializer_class(),
            OrderCreateSerializer,
        )


class OrderListCreateEndpointTests(BaseTestCase, TestListRequestSuccess, TestCreateRequestSuccess):
    def setUp(self):
        super().setUp()
        TestCreateRequestSuccess.setUp(self)
        self.view_url = reverse("list_create")
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderRetrieveUpdateDestroyEndpointTests(
    BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess
):
    def setUp(self):
        super().setUp()
        TestUpdateRequestSuccess.setUp(self)
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("retrieve_update_destroy", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithoutReadSerializerEndpointTests(BaseTestCase, TestListRequestSuccess):
    def setUp(self):
        super().setUp()
        self.view_url = reverse("list_without_read_serializer")
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveUpdateEndpointTests(
    BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess
):
    def setUp(self):
        super().setUp()
        TestUpdateRequestSuccess.setUp(self)
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("retrieve_update", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderCreateWithGenericEndpointTests(BaseTestCase, TestCreateRequestSuccess):
    def setUp(self):
        super().setUp()
        self.view_url = reverse("create")
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderUpdateWithGenericEndpointTests(BaseTestCase, TestUpdateRequestSuccess):
    def setUp(self):
        super().setUp()
        TestUpdateRequestSuccess.setUp(self)
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("update", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithGenericEndpointTests(BaseTestCase, TestListRequestSuccess):
    def setUp(self):
        super().setUp()
        self.view_url = reverse("list")
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveWithGenericEndpointTests(BaseTestCase, TestRetrieveRequestSuccess):
    def setUp(self):
        super().setUp()
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("retrieve", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
