# -*- coding: utf-8 -*-

from rest_framework import viewsets, mixins

from .generics import GenericAPIView
from .mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin


class GenericViewSet(GenericAPIView,
                     viewsets.GenericViewSet):
    pass


class ModelViewSet(CreateModelMixin,
                   RetrieveModelMixin,
                   UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   ListModelMixin,
                   GenericViewSet):
    pass


class ReadOnlyModelViewSet(RetrieveModelMixin,
                           ListModelMixin,
                           GenericViewSet):
    pass
