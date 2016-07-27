# -*- coding: utf-8 -*-
import os
from django.contrib.messages import constants

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SITE_ID = 1
TIME_ZONE = 'Europe/Moscow'
LANGUAGE_CODE = 'en-en'

USE_I18N = True
USE_L10N = True
USE_TZ = False
USE_THOUSAND_SEPARATOR = True

INSTALLED_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'crispy_forms',
    'app.flavors',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'app.urls'
WSGI_APPLICATION = 'app.wsgi.application'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.normpath(os.path.join(BASE_DIR, '..', 'static'))

GRAPPELLI_ADMIN_TITLE = 'Admin'

CRISPY_TEMPLATE_PACK = 'bootstrap3'

MEDIA_ROOT = os.path.normpath(os.path.join(BASE_DIR, '..', 'media'))
MEDIA_URL = '/media/'

FIXTURE_DIRS = (
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.debug',
                'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.request',
            )
        },
    },
]

MESSAGE_TAGS = {
    constants.ERROR: 'danger',
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'default-cache',
    },
    'core-cache': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'core-cache',
        'TIMEOUT': 60
    }
}
