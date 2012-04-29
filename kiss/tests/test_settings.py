DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

INSTALLED_APPS = (
    'django.contrib.sessions',
    'kiss',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'kiss.middleware.KissMiddleware',
)

SECRET_KEY = 'XXX'

KISS_API_KEY = 'XXX'
KISS_STORAGE='kiss.storage.session.SessionStorage'