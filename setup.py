#!/usr/bin/env python

from distutils.core import setup


setup(
    name='django-tatujs',
    version='0.1',
    description='TatuJS integration with Django.',
    author='Sophilabs',
    author_email='contact@sophilabs.com',
    url='https://github.com/sophilabs/django-tatujs/',
    packages=['tatujs'],
    requires=['BeautifulSoup4(>=4.2.0)'],
)
