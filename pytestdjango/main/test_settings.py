from main.settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'first',
    },
    'second': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'second',
    }
}
