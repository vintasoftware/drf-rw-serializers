Change Log
----------

..
   All enhancements and patches to drf_rw_serializers will be documented
   in this file.  It adheres to the structure of http://keepachangelog.com/ ,
   but in reStructuredText instead of Markdown (for ease of incorporation into
   Sphinx documentation and the PyPI description).

   This project adheres to Semantic Versioning (http://semver.org/).

.. There should always be an "Unreleased" section for changes pending release.

Unreleased
~~~~~~~~~~

[1.4.0] - 2024-06-05
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fixed
_____
* Fix a regression in the `get_read_serializer_class` and `get_write_serializer_class`
methods to return `get_serializer_class` as default.

[1.3.0] - 2024-06-03
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fixed
_____
* Re-add support for djangorestframework 3.14

[1.2.0] - 2024-05-27
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fixed
_____
* Fix a bug in the `get_serializer_class` method to return the appropriate serializer based on the request method, if any.

Removed
_______
* Drop support to Django 1.11
* Drop support to Django 2.0
* Drop support to Django 2.1
* Drop support to Django 2.2
* Drop support to Django 3.0
* Drop support to Django 3.1
* Drop support to Django 3.2
* Drop support to Django 4.0
* Drop support to Django 4.1
* Drop support to Python 3.7

[1.1.1] - 2024-02-07
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Fixed
_____
* Django 5.0 support fixed

[1.1.0] - 2023-12-22
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____
* Support Django 4.1
* Support Django 4.2
* Support Django 5.0
* Support Python 3.11
* Support Python 3.12

Fixed
_____
* Fixes CI workflow by migrating to GitHub Actions
* Fixes ReadTheDocs failing build

[1.0.5] - 2022-03-02
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____
* Support Django 3.2
* Support Django 4.0
* Support Python 3.10

[1.0.4] - 2020-09-02
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____
* Move from model-mommy to model-bakery
* Support Django 3.1


Removed
_______
* Drop support to Django 1.10
* Drop support to Python 2.7
* Drop support to Python 3.6

[1.0.2] - 2019-08-30
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Added
_____

* Support Django 2.2


[1.0.1] - 2019-01-16
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added
_____

* Fixed bug in retrieval of success headers in create endpoints (breaking change)
* Updated dependencies

[0.1.1] - 2018-11-12
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added
_____

* Support Django 2.1

[0.1.0] - 2018-02-21
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Added
_____

* First release on PyPI.
