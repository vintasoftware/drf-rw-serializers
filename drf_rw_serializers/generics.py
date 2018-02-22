# -*- coding: utf-8 -*-

from rest_framework import generics

from .mixins import CreateModelMixin, UpdateModelMixin


class GenericAPIView(generics.GenericAPIView):

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
        if not self.read_serializer_class:
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
        if not self.write_serializer_class:
            return self.get_serializer_class()
        
        return self.write_serializer_class


class CreateAPIView(CreateModelMixin, GenericAPIView, generics.CreateAPIView):
    pass


class UpdateAPIView(UpdateModelMixin, GenericAPIView, generics.UpdateAPIView):
    pass


class ListCreateAPIView(CreateModelMixin, GenericAPIView, generics.ListCreateAPIView):
    pass


class RetrieveUpdateAPIView(
        UpdateModelMixin, GenericAPIView, generics.RetrieveUpdateAPIView):
    pass


class RetrieveUpdateDestroyAPIView(
        UpdateModelMixin, GenericAPIView, generics.RetrieveUpdateDestroyAPIView):
    pass
