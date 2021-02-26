from .base import *



DEBUG = True

ALLOWED_HOSTS = ['portafolioappdev.herokuapp.com','127.0.0.1']


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'my_web',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'TIME_ZONE': 'UTC',
    }
}