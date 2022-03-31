=====
Usage
=====

To use Django REST Framework Read & Write Serializers in a project, you just
need to import some of the generic classes and use them to build your own
endpoints the same way you do with Django REST Framework generic views,
viwsets and mixins. The only difference is that instead of defining only one
serializer class for the view, now you can define a read_serializer_class and
a write_serializer_class that be used according to the method you are
implementing.

Eg.:

.. code-block:: python

    from drf_rw_serializers import generics
    from .models import MyModel
    from .serializers import MyModelReadSerializer, MyModelWriteSerializer


    class MyModelListCreateView(generics.ListCreateAPIView):
        queryset = MyModel.objects.all()
        read_serializer_class = MyModelReadSerializer
        write_serializer_class = MyModelWriteSerializer


If you need to dynamically override the serializers you can override the
following methods the same way you do with get_serializer_class and
get_serializer from Django REST Framework generic classes:

* get_read_serializer_class
* get_write_serializer_class
* get_read_serializer
* get_write_serializer


The drf_rw_serializers classes implementation doesn't break any of the
features Django REST Framework implements, so you can use the same way you
use DRF classes, but with the read and write serializers extra feature.

Eg.:

.. code-block:: python

    from drf_rw_serializers import generics
    from .models import MyModel
    from .serializers import MyModelWriteSerializer


    class MyModelListCreateView(generics.ListCreateAPIView):
        queryset = MyModel.objects.all()
        # this still works the way it works with DRF ListCreateAPIView
        serializer_class = MyModelWriteSerializer
