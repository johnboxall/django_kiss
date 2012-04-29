from django.utils.encoding import force_unicode, StrAndUnicode
from django.utils import simplejson


class Event(StrAndUnicode):
    def __init__(self, event):
        self.event = event

    def _prepare(self):
        self.event = simplejson.dumps(self.event)

    def __unicode__(self):
        return self.event


class BaseStorage(object):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        self._queued_events = []
        self.used = False
        self.added_new = False
        super(BaseStorage, self).__init__(*args, **kwargs)

    def __len__(self):
        return len(self._loaded_events) + len(self._queued_events)
    
    def __iter__(self):
        self.used = True
        if self._queued_events:
            self._loaded_events.extend(self._queued_events)
            self._queued_events = []
        return iter(self._loaded_events)

    @property
    def _loaded_events(self):
        if not hasattr(self, '_loaded_data'):
            events, all_retrieved = self._get()
            self._loaded_data = events or []
        return self._loaded_data

    def _prepare_events(self, events):
        for event in events:
            event._prepare()

    def update(self, response):
        self._prepare_events(self._queued_events)
        if self.used:
            return self._store(self._queued_events, response)
        elif self.added_new:
            events = self._loaded_events + self._queued_events
            return self._store(events, response)

    def add(self, event):
        self.added_new = True
        self._queued_events.append(Event(event))

    def _get(self, *args, **kwargs):
        raise NotImplementedError()

    def _store(self, events, response, *args, **kwargs):
        raise NotImplementedError()