# -*- coding: utf-8 -*-
from django.utils import version as django_version
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    OrderListCreateEndpoint, OrderRetrieveUpdateDestroyEndpoint,
    OrderRetrieveUpdateEndpoint, OrderCreateWithGenericEndpoint,
    OrderListWithGenericEndpoint, OrderRetrieveWithGenericEndpoint,
    OrderUpdateWithGenericEndpoint, OrderCreateWithMixinEndpoint,
    OrderUpdateWithMixinEndpoint, OrderListWithoutReadSerializerEndpoint,
    OrderListWithMixinEndpoint, OrderRetrieveWithMixinEndpoint,
    OrderViewset)

if django_version.get_complete_version() < (2, 0, 0):
    from django.conf.urls import url
else:
    from django.urls import re_path as url


urlpatterns = [
    url(r'^orders-list-without-read-serializer/$',
        OrderListWithoutReadSerializerEndpoint.as_view(),
        name='list_without_read_serializer'),

    url(r'^orders/$', OrderListCreateEndpoint.as_view(), name='list_create'),
    url(r'^orders/(?P<pk>[0-9]+)$', OrderRetrieveUpdateDestroyEndpoint.as_view(),
        name='retrieve_update_destroy'),
    url(r'^orders-retrieve-update/(?P<pk>[0-9]+)$', OrderRetrieveUpdateEndpoint.as_view(),
        name='retrieve_update'),
    url(r'^orders-list-generic-view/$', OrderListWithGenericEndpoint.as_view(),
        name='list'),
    url(r'^orders-retrieve-generic-view/(?P<pk>[0-9]+)$',
        OrderRetrieveWithGenericEndpoint.as_view(),
        name='retrieve'),
    url(r'^orders-create-generic-view/$', OrderCreateWithGenericEndpoint.as_view(),
        name='create'),
    url(r'^orders-update-generic-view/(?P<pk>[0-9]+)$', OrderUpdateWithGenericEndpoint.as_view(),
        name='update'),

    url(r'^orders-list-mixin/$', OrderListWithMixinEndpoint.as_view(),
        name='list_mixin'),
    url(r'^orders-retrieve-mixin/(?P<pk>[0-9]+)$', OrderRetrieveWithMixinEndpoint.as_view(),
        name='retrieve_mixin'),
    url(r'^orders-create-mixin/$', OrderCreateWithMixinEndpoint.as_view(),
        name='create_mixin'),
    url(r'^orders-update-mixin/(?P<pk>[0-9]+)$', OrderUpdateWithMixinEndpoint.as_view(),
        name='update_mixin'),

    url(r'^orders-viewset/$',
        OrderViewset.as_view({
            'get': 'list',
            'post': 'create',
        }),
        name='viewset_list_create'),
    url(r'^orders-viewset/(?P<pk>[0-9]+)$',
        OrderViewset.as_view({
            'get': 'retrieve',
            'put': 'update',
            'patch': 'partial_update',
            'delete': 'destroy',
        }),
        name='viewset_retrieve_update_destroy'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
