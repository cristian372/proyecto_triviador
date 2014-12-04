"""
Django settings for triviador project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
#RUTA_PROYECTO=os.path.dirname(os.path.realpath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = '0!m+#i-srv#q%25#kb0a+wcwlnoh%qtrw^y%&e$9#z&d09t5mq'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition


INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'social_auth',
    'bootstrap3',
    'triviador.apps.trivia',
    'triviador.apps.usuario',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS =  ( 
    'social.backends.facebook.FacebookOAuth2', 
    'django.contrib.auth.backends.ModelBackend', 
)

SOCIAL_AUTH_FACEBOOK_KEY =  '799491543451245' 
SOCIAL_AUTH_FACEBOOK_SECRET =  'd006f5c6bda00e084250c518b8adf810' 
SOCIAL_AUTH_FACEBOOK_SCOPE =  [ 'email' ]

LOGIN_REDIRECT_URL =  '/'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'


ROOT_URLCONF = 'triviador.urls'

WSGI_APPLICATION = 'triviador.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

#DATABASES = {
 #   'default': {
  #      'ENGINE': 'django.db.backends.sqlite3',
   #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    #}
#}
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'trivia',
        'USER': 'root',
        'PASSWORD':'',
        'HOST': '127.0.0.1', 
        'PORT' : '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'es-bo'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


TEMPLATE_DIRS=(
    os.path.join(BASE_DIR, "triviador/template"),
)
STATIC_URL = '/static/'
STATICFILES_DIRS=(
    os.path.join(BASE_DIR, "triviador/static"),
)
MEDIA_ROOT = os.path.join(BASE_DIR, "triviador/media")

LOGIN_URL = '/login/'

RECAPTCHA_PUBLIC_KEY = '6LfAzvwSAAAAAL39KH_Xdd2t2nkDJ--rhAorhtbf'
RECAPTCHA_PRIVATE_KEY = '6LfAzvwSAAAAABd6hjzru46AbI-7bcSjk1FM8vPY'
