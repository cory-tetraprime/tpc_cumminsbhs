from .base import *

DEBUG = True
DEBUG_PROPAGATE_EXCEPTIONS = False

SECRET_KEY = env('DJANGO_SECRET_KEY')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = env.int("DJANGO_SECURE_HSTS_SECONDS", default=2592000)
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool("DJANGO_SECURE_HSTS_INCLUDE_SUBDOMAINS", default=True)
SECURE_HSTS_PRELOAD = env.bool("DJANGO_SECURE_HSTS_PRELOAD", default=True)
SESSION_COOKIE_SECURE = env.bool("DJANGO_SESSION_COOKIE_SECURE", default=True)
CSRF_COOKIE_SECURE = env.bool("DJANGO_CSRF_COOKIE_SECURE", default=True)
CSRF_TRUSTED_ORIGINS = ['https://cummins.herokuapp.com']
ALLOWED_HOSTS = ["cummins.herokuapp.com", "localhost", "127.0.0.1", "0.0.0.0"]

DATABASES = {
    "default": env.dj_db_url("DATABASE_URL", default="postgres://postgres2@db/postgres2")
}

# STATICFILES_DIRS = [
#     '/',
# ]

SASS_PROCESSOR_INCLUDE_DIRS = [
    's3://cummins-web/',
]

STATIC_URL = "https://cummins-web.s3.amazonaws.com/"
MEDIA_URL = "/media/"
# Figure out what /media is used for.

INSTALLED_APPS = INSTALLED_APPS + ["storages"]
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
AWS_QUERYSTRING_AUTH = False
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = "private"
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME = 'us-east-1'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
