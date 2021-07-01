from django.http import HttpResponse
# Create your views here.
import logging

def info(msg):
    logger = logging.getLogger('command')
    logger.info(msg)


