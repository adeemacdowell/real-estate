import os

SILENCED_SYSTEM_CHECKS = ['urls.W002',]

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'job.scout.ri@gmail.com'
EMAIL_HOST_PASSWORD = 'bismila1'
DEFAULT_FROM_EMAIL = "Automated Email <job.scout.ri@gmail.com>"

ADMINS = (
    ('Adee Macdowell', 'adee@celtisaustralis.com'),
)

MANAGERS = ADMINS

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../'))

SITE_ID = 1

TIME_ZONE = 'America/Chicago'

USE_I18N = False

USE_L10N = False

USE_TZ = True

MEDIA_ROOT = os.path.join(SITE_ROOT, 'authweb', 'media')

MEDIA_URL = '/media/'

MEDIAFILES_DIRS = (
    os.path.join(SITE_ROOT, 'authweb', 'media'),
)

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(SITE_ROOT, 'authweb', 'static'),
]

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(SITE_ROOT, 'authweb', 'templates'),

        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'authweb.config.urls'

WSGI_APPLICATION = 'authweb.wsgi.application'
CRISPY_TEMPLATE_PACK = 'bootstrap4'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.humanize',
    'crispy_forms',

    # authweb Apps
    'authweb',
    'authweb.base',
    'authweb.main',
    'authweb.config',
    'authweb.realestate',
)

SECRET_KEY = '1i=u$$9865&pfr4l0qq9l7#fom+6%fj9h4-a&gvq^7p&d#hghl'





