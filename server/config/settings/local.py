
import os
from .base import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASSWORD'],
    }
}

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/')]

if DEBUG:
    def show_toolbar(request):
        return True


    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    # ここで表示する内容を設定できます↓↓基本的にはこれでok
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    }
