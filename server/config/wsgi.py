import os
from django.core.wsgi import get_wsgi_application
from dotenv import load_dotenv
load_dotenv('../.env')


application = get_wsgi_application()


envstate = os.getenv('ENV_STATE','local')
if envstate=='production':
    # settings/production.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')
elif envstate=='staging':
    # settings/staging.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.staging')
else:
    # settings/local.py
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')