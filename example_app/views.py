# -*- coding: utf-8 -*-

from drf_rw_serializers import generics, viewsets, mixins
from .models import Orders
from .serializers import OrderCreateSerializer, OrderListSerializer


class OrderListCreateEndpoint(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderRetrieveUpdateDestroyEndpoint(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderRetrieveUpdateEndpoint(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderCreateWithGenericEndpoint(generics.CreateAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderUpdateWithGenericEndpoint(generics.UpdateModelMixin):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderCreateWithMixinEndpoint(generics.GenericAPIView, mixins.CreateModelMixin):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderUpdateWithMixinEndpoint(generics.GenericAPIView, mixins.UpdateModelMixin):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, *kwargs):
        return self.partial_update(request, *args, **kwargs)


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer
