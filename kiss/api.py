import urllib
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import requests
from .storage import default_storage


def add_kiss(request, event):
    '''
    Push an event onto the kiss queue. eg.

    >>> add(request, ['alias', 'bob', 'bob@bob.com'])
    >>> add(request, ['record', 'Viewed Homepage', {'Campaign':'Print'}])

    `event` must be serializable into JSON. 
    It will be passed to _kmq.push({{ event}})

    '''
    if not hasattr(request, '_kiss'):
        raise ImproperlyConfigured('Requires kiss.middleware.KissMiddleware')
    return request._kiss.add(event)

def get_kiss(request):
    '''
    Returns an array of events queued on `request`.

    '''
    if hasattr(request, '_kiss'):
        return request._kiss
    return []

def track_kiss(identity, event_name, timestamp=None, api_key=settings.KISS_API_KEY, 
          fail_silently=False, **kwargs):
    '''
    Make a tracking HTTP request to the KM API.

    `api_key`: Your KM API Key.
    `event_name`: Name of the event to record.
    `identity`: Person doing the event.
    `timestamp`: Time the event occured in seconds as a UTC Unix epoch.
    `fail_silently`: Raise on errors.
    `kwargs`: Any additional event properties to send.

    http://support.kissmetrics.com/apis/specifications

    '''
    data = kwargs
    data['_n'] = event_name
    data['_p'] = identity
    data['_k'] = api_key

    if timestamp is not None:
        data['_t'] = timestamp
        data['_d'] = 1
    else:
        data['_t'] = int(time.time())

    qs = urllib.urlencode(data)
    url = 'http://trk.kissmetrics.com/e?%s' % qs

    try:
        response = requests.get(url, timeout=1)
    except Exception, e:
        if not fail_silently:
            raise
    else:
        if response.error and not fail_silently:
            raise response.error