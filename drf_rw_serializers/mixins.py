# -*- coding: utf-8 -*-

from rest_framework import mixins


class UpdateModelMixin(mixins.UpdateModelMixin):

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        write_serializer = self.get_write_serializer(
            instance, data=request.data, partial=partial)
        write_serializer.is_valid(raise_exception=True)
        self.perform_update(write_serializer)

        read_serializer = self.get_read_serializer(instance)
        
        return Response(read_serializer.data)


class CreateModelMixin(mixins.CreateModelMixin):

    def create(self, request, *args, **kwargs):
        write_serializer = self.get_write_serializer(data=request.data)
        write_serializer.is_valid(raise_exception=True)
        instance = self.perform_create(write_serializer)

        read_serializer = self.get_read_serializer(instance)
        
        return Response(read_serializer.data)