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
