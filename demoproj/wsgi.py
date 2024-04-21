"""
WSGI config for demoproj project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

ioption_settings:
    aws:elasticbeanstalk:container:python:
        WSGIPath: demoproj.wsgi:transferstavern
