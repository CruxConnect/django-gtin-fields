import os

# Helps when running this project through `django-admin runserver`.
DEBUG = True

INSTALLED_APPS = [
    'tests.app',
    'gtin_fields',  # The app with all your test models

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = tuple()

# Obvious rubbish
SECRET_KEY = 'not a secret'

# Add any URL routes needed for the tests in here
ROOT_URLCONF = 'tests.urls'

# Use sqlite by default. It is nice and snappy for small packages,
# and requires zero configuration.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.sqlite3',
    },
}

USE_TZ = True
TIME_ZONE = 'America/Denver'

STATIC_ROOT = os.path.join(os.path.dirname(__file__), 'static')
STATIC_URL = '/static/'
