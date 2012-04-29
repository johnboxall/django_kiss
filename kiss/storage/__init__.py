from django.conf import settings
from django.contrib.messages.storage import get_storage


default_storage = lambda request: get_storage(settings.KISS_STORAGE)(request)