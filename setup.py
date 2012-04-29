#!/usr/bin/env python
import codecs
import os
from setuptools import setup, find_packages


def read(*parts):
    return codecs.open(os.path.join(os.path.dirname(__file__), *parts)).read()


setup(
    name='django_kiss',
    version='0.1',
    description='A Django application for integrating KISSmetrics customer analytics',
    long_description=read('README.md'),
    author='John Boxall',
    author_email='john@mobify.com',
    url='http://github.com/johnboxall/django_kiss',
    packages=find_packages(),
    package_data={
        'kiss': [
            'templates/kiss/*'
        ]
    },
    include_package_data=True,
    install_requires=(
        'Django>=1.4',
        'requests'
    ),
    license=read('LICENSE'),
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Environment :: Web Environment',
        'Topic :: Internet :: WWW/HTTP',
    ),
)