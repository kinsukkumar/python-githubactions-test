"""
Django settings for web_rdt_project project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from . import dev_os_env #set on localhost
#from multisite import SiteID

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'app_rdt/static/'),
    os.path.join(BASE_DIR, 'microsoft_auth/static/'),
]


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

#ALLOWED_HOSTS = [
#    'localhost', 
#    '127.0.0.1',
#    'scbrdtseaaps001dev.azurewebsites.net',
#    '169.254.130.4',
#    '169.254.129.4'
#]

ALLOWED_HOSTS = ['*']

#MULTISITE_EXTRA_HOSTS = [
#    'localhost',
#    '127.0.0.1',
#    'scbrdtseaaps001dev.azurewebsites.net'
#]

# Application definition

INSTALLED_APPS = [
    'app_rdt.apps.ApprdtConfig',
    'users.apps.UsersConfig',
    'crispy_forms',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    #'microsoft_auth',
    'preventconcurrentlogins',
    'corsheaders',
    #'multisite',
]
SITE_ID = 1 #SiteID(default=1)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'csp.middleware.CSPMiddleware',
    'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
	'django.contrib.sites.middleware.CurrentSiteMiddleware',
    #'multisite.middleware.DynamicSiteMiddleware',
]

ROOT_URLCONF = 'web_rdt_project.urls'

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
                #'microsoft_auth.context_processors.microsoft',
            ],
        },
    },
]

WSGI_APPLICATION = 'web_rdt_project.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication'
    ]
}


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

RDT_CONFIG_DB_SCHEMA = os.environ.get('RDT_CONFIG_DB_SCHEMA')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASE_ROUTERS = ['web_rdt_project.db_routers.DBRouter']
DATABASE_APPS_MAPPING = {
    'app_rdt': 'default',
    'admin': 'default',
    'auth': 'default',
    'authtoken': 'default',
    'contenttypes': 'default',
    'sessions': 'default',
    'users': 'default',
    'preventconcurrentlogins': 'default',
    #'databrick':'dbrick_db',
    #auth, authtoken, contenttypes, sessions, users
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Bangkok'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

SESSION_EXPIRE_AT_BROWSER_CLOSE = True;
LOGIN_REDIRECT_URL = 'web-home'
LOGIN_URL = 'login'
LOGOUT_REDIRECT_URL = 'login'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '10.192.0.1'
EMAIL_PORT = 25
EMAIL_USE_TLS = False

APSCHEDULER_DATETIME_FORMAT =  "N j, Y, f:s a"  # Default

RDT_CONFIG_CUSTOM_WRITE_LOG = False
RDT_ADMIN_WRITE_LOG = False
RDT_SIGNIN_WRITE_LOG = False

RDT_REPORT_DIR = os.path.join(os.environ.get('RDT_APP_ENV_DIR'), 'app_rdt_reports/')

#security
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 15768000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
CSP_DEFAULT_SRC = ("'self'", 'app.powerbi.com')
CSP_FONT_SRC = ("'self'",'fonts.gstatic.com')
CSP_STYLE_SRC = ("'self'",'fonts.googleapis.com', "'unsafe-inline'")
CSP_OBJECT_SRC = ("'none'",)
CSP_IMG_SRC = ("'self'",'data:')
CSP_SCRIPT_SRC = ("'self'","'unsafe-inline'")

# CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = [
    'http://localhost:8000', 
    'http://127.0.0.1:8000',
    'https://scbrdtseaaps001dev.azurewebsites.net'
]
