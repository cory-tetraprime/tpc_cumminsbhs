from .base import *
import os


DEBUG = True  # SECURITY WARNING: don't run with debug turned on in production!

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django_errors.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# SECURITY WARNING: define the correct hosts in production!
# ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

SECRET_KEY = "django-insecure-#9$gh553_y^vd=3kg_&v#a#rny1%xw=&dsgxdo58+a1qd8qep*"

SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "cummins_main_1",
        "USER": "postgres",
        "PASSWORD": "T3tr@Pr1me",
        # "HOST": "172.31.160.1",
        "HOST": "192.168.1.75",
        "PORT": 5432
    }
}

STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"


# try:
#     from .local import *
# except ImportError:
#     pass
