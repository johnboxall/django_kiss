from django.conf import settings
from . import api


def kiss(request):
    '''
    Adds `kiss` and `KISS_API_KEY` to the context.

    '''
    return {
        'kiss': api.get_kiss(request),
        'KISS_API_KEY': settings.KISS_API_KEY
    }