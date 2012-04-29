from celery.decorators import task
from celery.task.sets import subtask
from .api import track as kiss_track


@task(ignore_result=True, default_retry_delay=30, max_retries=1, time_limit=5)
def track(identity, event_name, event_data=None, timestamp=None):
    event_data = event_data or {}

    try:
        kiss_track(identity, event_name, timestamp, **event_data)
    except Exception, exc:
        track.retry(exc=exc)