# -*- coding: utf-8 -*-

from rest_framework import generics, mixins

from .mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)


class GenericAPIView(generics.GenericAPIView):
    def _get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        assert (
            self.serializer_class is not None
            or getattr(self, "read_serializer_class", None) is not None
        ), (
            "'%s' should either include one of `serializer_class` and `read_serializer_class` "
            "attribute, or override one of the `get_serializer_class()`, "
            "`get_read_serializer_class()` method." % self.__class__.__name__
        )

        return self.serializer_class

    def get_serializer_class(self):
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
                return self.get_read_serializer_class()

            if self.request.method in ["POST", "PUT", "PATCH", "DELETE"]:
                assert (
                    getattr(self, "write_serializer_class", None) is not None
                    or self.serializer_class is not None
                ), (
                    "'%s' should either include a `write_serializer_class` or `serializer_class` "
                    "attribute, or override the `get_write_serializer_class()` or "
                    "`get_serializer_class()` method." % self.__class__.__name__
                )
                return self.get_write_serializer_class()

        return self._get_serializer_class()

    def get_read_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for serializing output.
        """
        serializer_class = self.get_read_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_read_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.read_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        if getattr(self, "read_serializer_class", None) is None:
            return self._get_serializer_class()

        return self.read_serializer_class

    def get_write_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating
        and deserializing input.
        """
        serializer_class = self.get_write_serializer_class()
        kwargs["context"] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_write_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.write_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins can send extra fields, others cannot)
        """
        if getattr(self, "write_serializer_class", None) is None:
            return self._get_serializer_class()

        return self.write_serializer_class


class CreateAPIView(CreateModelMixin, GenericAPIView):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateAPIView(UpdateModelMixin, GenericAPIView):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ListAPIView(ListModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveAPIView(RetrieveModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveDestroyAPIView(RetrieveModelMixin, mixins.DestroyModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RetrieveUpdateAPIView(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class RetrieveUpdateDestroyAPIView(
    RetrieveModelMixin, UpdateModelMixin, mixins.DestroyModelMixin, GenericAPIView
):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
