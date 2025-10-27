# -*- coding: utf-8 -*-

from rest_framework import mixins, viewsets

from .generics import GenericAPIView, _MT_co
from .mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin


class GenericViewSet(GenericAPIView[_MT_co], viewsets.GenericViewSet[_MT_co]):
    pass


class ModelViewSet(
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    mixins.DestroyModelMixin,
    ListModelMixin,
    GenericViewSet[_MT_co],
):
    pass


class ReadOnlyModelViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet[_MT_co]):
    pass
