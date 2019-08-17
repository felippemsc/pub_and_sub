#!/usr/bin/env python
import os
import unittest

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "README.md")) as f:
    long_description = f.read()

requires = [
    'click==7.0',
    'falcon==2.0.0',
    'gunicorn==19.9.0',
    'pika==1.1.0'
]

tests_require = [
    'coverage==4.5.4',
    'pycodestyle==2.5.0',
    'pylint==2.3.1'
]

setup_requires = ['pytest-runner']


def my_test_suite():
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('tests', pattern='test_*.py')
    return test_suite


setup(
    name=u"Publisher and Subscriber",
    version="0.0.1",
    description=u"Publisher and Subscriber Service",
    long_description=long_description,
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Falcon',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Felippe Costa',
    author_email='felippemsc@gmai.com',
    python_requires='>=3.7',
    packages=find_packages(exclude='tests'),
    install_requires=requires,
    test_suite='tests',
    setup_requires=setup_requires,
    tests_require=tests_require
)