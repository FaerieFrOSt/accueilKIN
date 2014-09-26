"""
Django settings for intra project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'urdc-apv*p0iw*d4se1s!+#bsrnfrsz8@x906+bs2enl!2zg6o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
	'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'kfet',
	'users',
	'tags',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'intra.urls'

WSGI_APPLICATION = 'intra.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'radcheck':
    {
        'NAME': 'radius',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': ''
    }
}

DATABASE_ROUTERS = ['intra.AuthRouter.AuthRouter']

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOGIN_URL = '/login/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_FINDER = (
		'django.contrib.staticfiles.finder.AppDirectoriesFinder',
		'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATIC_URL = '/static/'

STATICFILES_DIRS = ('static/',)

TEMPLATE_DIRS = ('templates/',)

TEMPLATE_CONTEXT_PROCESSORS = (
		"django.contrib.auth.context_processors.auth",
		"django.core.context_processors.debug",
		"django.core.context_processors.i18n",
		"django.core.context_processors.media",
		"django.core.context_processors.static",
		"django.core.context_processors.tz",
		"django.contrib.messages.context_processors.messages",
		"intra.context_processors.getTitle",
		"intra.context_processors.getGadz",
		"django.core.context_processors.request",
		)
