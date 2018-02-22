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


class ListModelMixin(mixins.ListModelMixin):

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_read_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class RetrieveModelMixin(mixins.RetrieveModelMixin):

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_read_serializer(instance)
        return Response(serializer.data)
