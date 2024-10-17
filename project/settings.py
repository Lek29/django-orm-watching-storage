import os
from dotenv import load_dotenv


load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'HOST': 'checkpoint.devman.org',
        'PORT': '5434',
        'NAME': 'checkpoint',
        'USER': 'guard',
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG', 'False').lower() in ['true', ]

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
