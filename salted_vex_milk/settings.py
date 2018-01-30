"""
Django settings for salted_vex_milk project.

Generated by 'django-admin startproject' using Django 2.0.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os
import logging
from django.core.exceptions import ImproperlyConfigured



logging.basicConfig(format = '%(asctime)s - %(levelname)s - %(message)s',
                    datefmt =' %m/%d/%y %H:%M:%S')
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
logger.debug(f"base_dir: {BASE_DIR}")

# SECURITY WARNING: keep the secret key used in production secret!
def get_env_variable(var_name):
    """get environmental variable, or return exception
    Taken from Section 5.3.5 Two Scoops"""
    try:
        return os.environ.get(var_name)
    except KeyError:
        error_msg = 'get_env_variable error: Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_variable('SECRET_KEY')
D2_KEY =  get_env_variable('D2_KEY')
DEBUG = get_env_variable('DEBUG')

logger.debug(f"Debug setting: {DEBUG}")


# Application definition

INSTALLED_APPS = [
    #django built-ins
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #third-party apps
    'django_tables2',

    #my apps
    'd2api',
    'clans',
    'members',
    'characters',


]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'salted_vex_milk.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'salted_vex_milk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vexdata',
        'USER': 'eric',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

"""
#PREVIOUS WAY: not great
### Static files (CSS, JavaScript, Images)
### https://docs.djangoproject.com/en/1.11/howto/static-files/
#STATIC_URL = '/static/'
#
##Static asset configuration [new from https://devcenter.heroku.com/articles/django-assets]
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')  #'staticfiles'
logger.debug(f"project_root: {PROJECT_ROOT}")
"""

##########################
# Static files (CSS, JavaScript, Images) are collected and put here
# https://docs.djangoproject.com/en/1.9/howto/static-files/
#"The default is to look in all locations defined in STATICFILES_DIRS and
#in the 'static' directory of apps specified by the INSTALLED_APPS setting."
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  #where they will be saved for serving
STATIC_URL = '/static/'
#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
STATICFILES_DIRS = (
        os.path.join(BASE_DIR, 'static'),
        ) #where it will get any extras
logger.debug(f"BASE_DIR: {BASE_DIR}")
logger.debug(f"static_root: {STATIC_ROOT}")
logger.debug(f"staticfiles_dirs: {STATICFILES_DIRS}")
#
# Extra places for collectstatic to find static files if you aren't putting them
#in the usual places for apps.
#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)
#logger.debug(f"STATIFILES_DIRS: {STATICFILES_DIRS}")


################
#Server settings
################
ALLOWED_HOSTS =  ['localhost', 'svm-dev.herokuapp.com', 'saltedvexmilk.herokuapp.com']
#Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = {'HTTP_X_FORWARDED_PROTO', 'https'}  #can be on localhost

# Update database configuration with $DATABASE_URL, as recommended at:
# https://devcenter.heroku.com/articles/django-app-configuration
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
#Following generates 500 error when not commented out :()
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



