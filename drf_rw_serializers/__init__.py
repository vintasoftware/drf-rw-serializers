"""
Generic views, viewsets and mixins that extend the Django REST Framework ones adding
separated serializers for read and write operations.
"""

from __future__ import absolute_import, unicode_literals

__version__ = '1.0.5'

# pylint: disable=invalid-name
default_app_config = 'drf_rw_serializers.apps.DrfRwSerializersConfig'
# pylint: enable=invalid-name
