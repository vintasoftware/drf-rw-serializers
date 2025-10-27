# -*- coding: utf-8 -*-
from typing import Any, TypeVar, Union

from django.db.models import Model

from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import BaseSerializer

from .mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

_MT_co = TypeVar("_MT_co", bound=Model, covariant=True)


class GenericAPIView(generics.GenericAPIView[_MT_co]):
    read_serializer_class: Union[type[BaseSerializer[_MT_co]], None] = None
    write_serializer_class: Union[type[BaseSerializer[_MT_co]], None] = None

    def get_serializer_class(self) -> type[BaseSerializer[_MT_co]]:
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.

        If the request method is GET, it tries to use `self.read_serializer_class`.
        If the request method is not GET, it tries to use `self.write_serializer_class`.
        If the specific serializer class for the request method is not set, it falls back to
        `self.serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        if hasattr(self, "request"):
            if self.request.method in ["GET", "HEAD", "OPTIONS", "TRACE"]:
                assert (
                    getattr(self, "read_serializer_class", None) is not None
                    or self.serializer_class is not None
                ), (
                    "'%s' should either include a `read_serializer_class` or `serializer_class` "
                    "attribute, or override the `get_read_serializer_class()` or "
                    "`get_serializer_class()` method." % self.__class__.__name__
                )
                # `default_to_serializer_class` is used to prevent a `RecursionError`
                return self.get_read_serializer_class(default_to_serializer_class=True)

            if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
                assert (
                    getattr(self, "write_serializer_class", None) is not None
                    or self.serializer_class is not None
                ), (
                    "'%s' should either include a `write_serializer_class` or `serializer_class` "
                    "attribute, or override the `get_write_serializer_class()` or "
                    "`get_serializer_class()` method." % self.__class__.__name__
                )
                # `default_to_serializer_class` is used to prevent a `RecursionError`
                return self.get_write_serializer_class(default_to_serializer_class=True)

        assert (
            self.serializer_class is not None
            or getattr(self, "read_serializer_class", None) is not None
        ), (
            "'%s' should either include one of `serializer_class` and `read_serializer_class` "
            "attribute, or override one of the `get_serializer_class()`, "
            "`get_read_serializer_class()` method." % self.__class__.__name__
        )

        return super().get_serializer_class()

    def get_read_serializer(self, *args: Any, **kwargs: Any) -> BaseSerializer[_MT_co]:
        """
        Return the serializer instance that should be used for serializing output.
        """
        serializer_class = self.get_read_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_read_serializer_class(
        self, default_to_serializer_class: bool = False
    ) -> type[BaseSerializer[_MT_co]]:
        """
        Return the class to use for the serializer.
        Defaults to using `self.read_serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins get full serialization, others get basic serialization)
        """
        if self.read_serializer_class is None:
            if default_to_serializer_class:
                return super().get_serializer_class()

            return self.get_serializer_class()

        return self.read_serializer_class

    def get_write_serializer(self, *args: Any, **kwargs: Any) -> BaseSerializer[_MT_co]:
        """
        Return the serializer instance that should be used for validating
        and deserializing input.
        """
        serializer_class = self.get_write_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_write_serializer_class(
        self, default_to_serializer_class: bool = False
    ) -> type[BaseSerializer[_MT_co]]:
        """
        Return the class to use for the serializer.
        Defaults to using `self.write_serializer_class`.

        You may want to override this if you need to provide different
        serializations depending on the incoming request.

        (Eg. admins can send extra fields, others cannot)
        """
        if self.write_serializer_class is None:
            if default_to_serializer_class:
                return super().get_serializer_class()

            return self.get_serializer_class()

        return self.write_serializer_class


class CreateAPIView(CreateModelMixin, GenericAPIView[_MT_co]):
    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.create(request, *args, **kwargs)


class UpdateAPIView(UpdateModelMixin, GenericAPIView[_MT_co]):
    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.partial_update(request, *args, **kwargs)


class ListAPIView(ListModelMixin, GenericAPIView[_MT_co]):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.list(request, *args, **kwargs)


class RetrieveAPIView(RetrieveModelMixin, GenericAPIView[_MT_co]):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.retrieve(request, *args, **kwargs)


class ListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView[_MT_co]):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.create(request, *args, **kwargs)


class RetrieveDestroyAPIView(RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView[_MT_co]):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.destroy(request, *args, **kwargs)


class RetrieveUpdateAPIView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView[_MT_co]):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.partial_update(request, *args, **kwargs)


class RetrieveUpdateDestroyAPIView(
    RetrieveModelMixin, UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView[_MT_co]
):
    def get(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.update(request, *args, **kwargs)

    def patch(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        return self.destroy(request, *args, **kwargs)
