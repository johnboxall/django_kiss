# Django Kiss

A Django application for integrating KISSmetrics customer analytics.

KISSmetrics recommends developers record events using their JavaScript API, however it can be difficult to tell when to record an event using only client side code. For example, how does the client know when a form is successfully submitted?

Django Kiss uses the Django Session Framework to record events against a users session. The recorded in the session are then written out to an HTML page as JavaScript. The user's browser executes the JavaScript, firing the tracking requests to the KM API.

----

## Installation

* Install the package.

* Update your `settings.py`:

    INSTALLED_APPS += ('kiss',)
    MIDDLEWARE_CLASSES += ('kiss.middleware.KissMiddleware',)

    KISS_API_KEY = 'YOUR_KM_API_KEY'
    KISS_STORAGE = 'kiss.storage.session.SessionStorage'

* Django Kiss requires the Django Session Framework to be installed.

## Usage

Recording an event with Django Kiss is a two step process. First an event must be recorded against a request using `kiss.add_kiss`. Second, the user's browser must load a page with KM tracking JavaScript.

Record an event against the user's sessions:

    import kiss

    def view(request):
        kiss.add_kiss(request, ['record', 'event_name'])
        ...

Include `kiss/core.html` in your base template to write out KM tracking JavaScripts and the events stored against the user's session:

    {% include 'kiss/core.html' %}

To associate a particular request with an identity you can add a signal listener:

    from django.contrib.auth import signals as auth_signals

    @receiver(auth_signals.user_logged_in)
    def user_logged_in_kiss(sender, **kwargs):
        request = kwargs['request']
        user = kwargs['user']
        kiss.add_kiss(request, ['identify', user.email])
        kiss.add_kiss(request, ['record', 'login'])

## Tests

To run the tests:

    django-admin.py test kiss --settings=kiss.tests.test_settings