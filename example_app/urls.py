# -*- coding: utf-8 -*-
from django.urls import path, re_path

from rest_framework.urlpatterns import format_suffix_patterns

from .views import (
    OrderCreateWithGenericEndpoint,
    OrderCreateWithMixinEndpoint,
    OrderListCreateEndpoint,
    OrderListWithGenericEndpoint,
    OrderListWithMixinEndpoint,
    OrderListWithoutReadSerializerEndpoint,
    OrderRetrieveUpdateDestroyEndpoint,
    OrderRetrieveUpdateEndpoint,
    OrderRetrieveWithGenericEndpoint,
    OrderRetrieveWithMixinEndpoint,
    OrderUpdateWithGenericEndpoint,
    OrderUpdateWithMixinEndpoint,
    OrderViewset,
)

urlpatterns = [
    path(
        "orders-list-without-read-serializer/",
        OrderListWithoutReadSerializerEndpoint.as_view(),
        name="list_without_read_serializer",
    ),
    path("orders/", OrderListCreateEndpoint.as_view(), name="list_create"),
    re_path(
        r"^orders/(?P<pk>[0-9]+)$",
        OrderRetrieveUpdateDestroyEndpoint.as_view(),
        name="retrieve_update_destroy",
    ),
    re_path(
        r"^orders-retrieve-update/(?P<pk>[0-9]+)$",
        OrderRetrieveUpdateEndpoint.as_view(),
        name="retrieve_update",
    ),
    path("orders-list-generic-view/", OrderListWithGenericEndpoint.as_view(), name="list"),
    re_path(
        r"^orders-retrieve-generic-view/(?P<pk>[0-9]+)$",
        OrderRetrieveWithGenericEndpoint.as_view(),
        name="retrieve",
    ),
    path("orders-create-generic-view/", OrderCreateWithGenericEndpoint.as_view(), name="create"),
    re_path(
        r"^orders-update-generic-view/(?P<pk>[0-9]+)$",
        OrderUpdateWithGenericEndpoint.as_view(),
        name="update",
    ),
    path("orders-list-mixin/", OrderListWithMixinEndpoint.as_view(), name="list_mixin"),
    re_path(
        r"^orders-retrieve-mixin/(?P<pk>[0-9]+)$",
        OrderRetrieveWithMixinEndpoint.as_view(),
        name="retrieve_mixin",
    ),
    path("orders-create-mixin/", OrderCreateWithMixinEndpoint.as_view(), name="create_mixin"),
    re_path(
        r"^orders-update-mixin/(?P<pk>[0-9]+)$",
        OrderUpdateWithMixinEndpoint.as_view(),
        name="update_mixin",
    ),
    path(
        "orders-viewset/",
        OrderViewset.as_view(
            {
                "get": "list",
                "post": "create",
            }
        ),
        name="viewset_list_create",
    ),
    re_path(
        r"^orders-viewset/(?P<pk>[0-9]+)$",
        OrderViewset.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
        name="viewset_retrieve_update_destroy",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
