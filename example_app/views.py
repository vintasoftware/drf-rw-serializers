# -*- coding: utf-8 -*-

from drf_rw_serializers import generics, mixins, viewsets

from .models import Order
from .serializers import OrderCreateSerializer, OrderListSerializer


class OrderListCreateEndpoint(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderListWithoutReadSerializerEndpoint(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer


class OrderRetrieveUpdateDestroyEndpoint(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderRetrieveUpdateEndpoint(generics.RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderCreateWithGenericEndpoint(generics.CreateAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderUpdateWithGenericEndpoint(generics.UpdateAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderListWithGenericEndpoint(generics.ListAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderRetrieveWithGenericEndpoint(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer


class OrderCreateWithMixinEndpoint(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class OrderUpdateWithMixinEndpoint(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class OrderListWithMixinEndpoint(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderRetrieveWithMixinEndpoint(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    read_serializer_class = OrderListSerializer
    write_serializer_class = OrderCreateSerializer
