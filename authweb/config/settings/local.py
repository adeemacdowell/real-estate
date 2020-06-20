from .base import *

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

STATIC_ROOT = ""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'authweb',                      # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': 'N0F0r3!gnK3y$',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

EMAIL_HOST_PASSWORD = '>:#gd"dq.M36X+%M'



