# -*- coding: utf-8 -*-

from rest_framework import viewsets

from .generics import GenericAPIView
from .mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin


class GenericViewSet(GenericAPIView, viewsets.GenericViewSet):
    pass


class ModelViewSet(
        CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin, 
        GenericAPIView, viewsets.ModelViewSet):
    pass


class ReadOnlyModelViewSet(
        ListModelMixin, RetrieveModelMixin, GenericAPIView, viewsets.ReadOnlyModelViewSet):
    pass
