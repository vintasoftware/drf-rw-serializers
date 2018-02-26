# -*- coding: utf-8 -*-

from rest_framework import generics

from .mixins import CreateModelMixin, UpdateModelMixin, ListModelMixin, RetrieveModelMixin


class GenericAPIView(generics.GenericAPIView):

    def get_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        assert (
            self.serializer_class is not None or
            getattr(self, 'read_serializer_class', None) is not None
        ), (
            "'%s' should either include one of `serializer_class` and `read_serializer_class` "
            "attribute, or override one of the `get_serializer_class()`, "
            "`get_read_serializer_class()` method."
            % self.__class__.__name__
        )

        return self.serializer_class

    def get_read_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for serializing output.
        """
        serializer_class = self.get_read_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_read_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.read_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins get full serialization, others get basic serialization)
        """
        if getattr(self, 'read_serializer_class', None) is None:
            return self.get_serializer_class()

        return self.read_serializer_class

    def get_write_serializer(self, *args, **kwargs):
        """
        Return the serializer instance that should be used for validating
        and deserializing input.
        """
        serializer_class = self.get_write_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)

    def get_write_serializer_class(self):
        """
        Return the class to use for the serializer.
        Defaults to using `self.write_serializer_class`.
        You may want to override this if you need to provide different
        serializations depending on the incoming request.
        (Eg. admins can send extra fields, others cannot)
        """
        if getattr(self, 'write_serializer_class', None) is None:
            return self.get_serializer_class()

        return self.write_serializer_class


class CreateAPIView(CreateModelMixin, generics.CreateAPIView, GenericAPIView):
    pass


class UpdateAPIView(UpdateModelMixin, generics.UpdateAPIView, GenericAPIView):
    pass


class ListAPIView(ListModelMixin, generics.ListAPIView, GenericAPIView):
    pass


class RetrieveAPIView(
        RetrieveModelMixin, generics.RetrieveAPIView, GenericAPIView):
    pass


class ListCreateAPIView(
        CreateModelMixin, ListModelMixin, generics.ListCreateAPIView, GenericAPIView):
    pass


class RetrieveDestroyAPIView(
        RetrieveModelMixin, generics.RetrieveDestroyAPIView, GenericAPIView):
    pass


class RetrieveUpdateAPIView(
        UpdateModelMixin, RetrieveModelMixin, generics.RetrieveUpdateAPIView, GenericAPIView):
    pass


class RetrieveUpdateDestroyAPIView(
        UpdateModelMixin, RetrieveModelMixin, generics.RetrieveUpdateDestroyAPIView,
        GenericAPIView):
    pass
