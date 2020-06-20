from .base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'authweb',                      # Or path to database file if using sqlite3.
        'USER': 'root',
        'PASSWORD': os.environ['DATABASE_PASSWORD'],
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']


SECURE_SSL_REDIRECT = True
SECURE_REDIRECT_EXEMPT = ["^firstapp/"]
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SESSION_COOKIE_SECURE = True
X_FRAME_OPTIONS = "DENY"
CSRF_COOKIE_SECURE = True


ALLOWED_HOSTS = [
    'in-every-respect.com',
]

STATIC_ROOT = "/home/ubuntu/static"
MEDIA_ROOT = "/home/ubuntu/authweb/authweb/media"




