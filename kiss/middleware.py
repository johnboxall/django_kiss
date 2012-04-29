from django.conf import settings
from .api import default_storage


class KissMiddleware(object):
    def process_request(self, request):
        request._kiss = default_storage(request)

    def process_response(self, request, response):
        if hasattr(request, '_kiss'):
            unstored_messages = request._kiss.update(response)
            if unstored_messages and settings.DEBUG:
                raise ValueError('Not all Kiss Events could be stored.')
        return response
