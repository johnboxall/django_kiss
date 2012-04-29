from .base import BaseStorage


class SessionStorage(BaseStorage):
    session_key = '_kiss'

    def __init__(self, request, *args, **kwargs):
        super(SessionStorage, self).__init__(request, *args, **kwargs)

    def _get(self, *args, **kwargs):
        return self.request.session.get(self.session_key), True

    def _store(self, events, response, *args, **kwargs):
        if events:
            self.request.session[self.session_key] = events
        else:
            self.request.session.pop(self.session_key, None)
        return []