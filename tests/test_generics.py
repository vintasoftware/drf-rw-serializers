#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for the `drf-rw-serializers` models module.
"""

from __future__ import absolute_import, unicode_literals

from unittest import mock

from django.utils import version as django_version

import pytest
from model_bakery import baker

from drf_rw_serializers import generics
from example_app.serializers import OrderCreateSerializer, OrderListSerializer
from test_utils.base_tests import (
    BaseTestCase,
    TestCreateRequestSuccess,
    TestListRequestSuccess,
    TestRetrieveRequestSuccess,
    TestUpdateRequestSuccess,
)


if django_version.get_complete_version() < (2, 0, 0):
    from django.core.urlresolvers import reverse  # pylint: disable=no-name-in-module,import-error
else:
    from django.urls import reverse  # pylint: disable=no-name-in-module,import-error


class GenericAPIViewGetSerializerClassTests(BaseTestCase):
    def test_serializer_class_not_provided(self):
        class NoSerializerClass(generics.GenericAPIView):
            pass

        with pytest.raises(AssertionError) as excinfo:
            NoSerializerClass().get_serializer_class()

        self.assertEqual(
            str(excinfo.value),
            (
                "'NoSerializerClass' should either include one of `serializer_class` "
                "and `read_serializer_class` attribute, or override one of the "
                "`get_serializer_class()`, `get_read_serializer_class()` method."
            ),
        )

    def test_prioritize_serializer_class(self):
        class PrioritizeSerializerClass(generics.GenericAPIView):
            serializer_class = OrderListSerializer
            read_serializer_class = OrderListSerializer
            write_serializer_class = OrderCreateSerializer

        self.assertEqual(PrioritizeSerializerClass().get_serializer_class(), OrderListSerializer)


class GenericAPIViewGetReadSerializerClassTests(BaseTestCase):
    def test_read_serializer_class_not_provided(self):
        class NoReadSerializerClass(generics.GenericAPIView):
            pass

        with mock.patch.object(
            NoReadSerializerClass, "_get_serializer_class"
        ) as mock__get_serializer_class:
            NoReadSerializerClass().get_read_serializer_class()

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
        class NoWriteSerializerClass(generics.GenericAPIView):
            pass

        with mock.patch.object(
            NoWriteSerializerClass, "_get_serializer_class"
        ) as mock__get_serializer_class:
            NoWriteSerializerClass().get_write_serializer_class()

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
        super(OrderListCreateEndpointTests, self).setUp()
        TestCreateRequestSuccess.setUp(self)
        self.view_url = reverse("list_create")
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer

    # def test_get_serializer_class(self):
    #     # GET request
    #     response = self.auth_client.get(self.view_url, format="json")
    #     view = response.renderer_context["view"]
    #     self.assertEqual(view.get_serializer_class(), OrderListSerializer)

    #     # POST request
    #     response = self.auth_client.post(
    #         self.view_url,
    #         {
    #             "table_number": 100,
    #             "ordered_meals": [
    #                 {
    #                     "quantity": 1,
    #                     "meal": self.meals[0].id,
    #                 },
    #                 {
    #                     "quantity": 2,
    #                     "meal": self.meals[1].id,
    #                 },
    #             ],
    #         },
    #         format="json",
    #     )
    #     view = response.renderer_context["view"]
    #     self.assertEqual(view.get_serializer_class(), OrderCreateSerializer)


class OrderRetrieveUpdateDestroyEndpointTests(
    BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess
):

    def setUp(self):
        super(OrderRetrieveUpdateDestroyEndpointTests, self).setUp()
        TestUpdateRequestSuccess.setUp(self)
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("retrieve_update_destroy", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithoutReadSerializerEndpointTests(BaseTestCase, TestListRequestSuccess):

    def setUp(self):
        super(OrderListWithoutReadSerializerEndpointTests, self).setUp()
        self.view_url = reverse("list_without_read_serializer")
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveUpdateEndpointTests(
    BaseTestCase, TestRetrieveRequestSuccess, TestUpdateRequestSuccess
):

    def setUp(self):
        super(OrderRetrieveUpdateEndpointTests, self).setUp()
        TestUpdateRequestSuccess.setUp(self)
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("retrieve_update", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderCreateWithGenericEndpointTests(BaseTestCase, TestCreateRequestSuccess):

    def setUp(self):
        super(OrderCreateWithGenericEndpointTests, self).setUp()
        self.view_url = reverse("create")
        self.list_serializer_class = OrderListSerializer
        self.create_in_serializer_class = OrderCreateSerializer
        self.create_out_serializer_class = OrderListSerializer


class OrderUpdateWithGenericEndpointTests(BaseTestCase, TestUpdateRequestSuccess):

    def setUp(self):
        super(OrderUpdateWithGenericEndpointTests, self).setUp()
        TestUpdateRequestSuccess.setUp(self)
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("update", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
        self.update_in_serializer_class = OrderCreateSerializer
        self.update_out_serializer_class = OrderListSerializer


class OrderListWithGenericEndpointTests(BaseTestCase, TestListRequestSuccess):

    def setUp(self):
        super(OrderListWithGenericEndpointTests, self).setUp()
        self.view_url = reverse("list")
        self.list_serializer_class = OrderListSerializer


class OrderRetrieveWithGenericEndpointTests(BaseTestCase, TestRetrieveRequestSuccess):

    def setUp(self):
        super(OrderRetrieveWithGenericEndpointTests, self).setUp()
        self.object = baker.make("example_app.Order")
        baker.make("example_app.OrderedMeal", order=self.object, _quantity=2)
        self.view_url = reverse("retrieve", kwargs={"pk": self.object.pk})
        self.retrieve_serializer_class = OrderListSerializer
