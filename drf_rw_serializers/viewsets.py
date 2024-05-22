# -*- coding: utf-8 -*-

from rest_framework import mixins, viewsets

from .generics import GenericAPIView
from .mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin


class GenericViewSet(GenericAPIView, viewsets.GenericViewSet):
    pass


class ModelViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    mixins.DestroyModelMixin,
    ListModelMixin,
    GenericViewSet,
):
    pass


class ReadOnlyModelViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    pass
