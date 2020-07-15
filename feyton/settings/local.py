from decouple import config

from .base import *

DEBUG = True
ALLOWED_HOSTS = []

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = 'no-reply@feyton.co.rw'


DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
