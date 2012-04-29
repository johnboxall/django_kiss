from django.core.handlers.base import BaseHandler
from django.test import TestCase
from django.test.client import RequestFactory as BaseRequestFactory
from .. import api


class RequestFactory(BaseRequestFactory):
    '''
    `RequestFactory` that applies request middleware to requests.

    '''
    def request(self, **request):
        request = super(RequestFactory, self).request(**request)
        handler = BaseHandler()
        handler.load_middleware()
        for middleware_method in handler._request_middleware:
            if middleware_method(request):
                raise Exception('request middleware returned a response')
        return request


class APITest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_add_kiss(self):
        request = self.factory.get('/')
        api.add_kiss(request, ['record', 'test_add'])

    def test_get(self):
        request = self.factory.get('/')
        api.add_kiss(request, ['record', 'test_add'])
        events = api.get_kiss(request)