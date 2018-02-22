# -*- coding: utf-8 -*-

from rest_framework import viewsets

from .generics import GenericAPIView
from .mixins import CreateModelMixin, UpdateModelMixin


class GenericViewSet(GenericAPIView, viewsets.GenericViewSet):
    pass


class ModelViewSet(
        CreateModelMixin, UpdateModelMixin, GenericAPIView, 
        viewsets.ModelViewSet):
    pass


class ReadOnlyModelViewSet(
        GenericAPIView, viewsets.ReadOnlyModelViewSet):
    pass