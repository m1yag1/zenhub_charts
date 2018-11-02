from .settings import *  # noqa
import os

GITHUB = {
    'token': os.environ['GITHUB_TOKEN'],
    'owner': os.environ['GITHUB_OWNER']
}
ZENHUB = {
    'token': os.environ['ZENHUB_TOKEN']
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'zenhub_charts'),
        'USER': os.environ.get('DB_USER', 'postgres'),
        'PASSWORD': os.environ.get('DB_PASSWORD', None),
        'HOST': os.environ.get('DB_HOST', 'db'),
        'PORT': os.environ.get('DB_PORT', None)
    }
}


CELERY_BROKER_URL = os.environ['CELERY_BROKER_URL']
CELERY_RESULT_BACKEND = 'redis'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']
