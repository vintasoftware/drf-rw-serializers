"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

from __future__ import absolute_import, unicode_literals

from os.path import abspath, dirname, join


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "rest_framework",
    "example_app",
)

LOCALE_PATHS = [
    root("drf_rw_serializers", "conf", "locale"),
]

ROOT_URLCONF = "example_app.urls"

SECRET_KEY = "insecure-secret-key"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
