# coding: utf-8
from setuptools import setup

setup(
    name='django-debug-panel',
    version='0.8.3',
    author=u'Joël Billaud',
    author_email='jbillaud@gmail.com',
    packages=['debug_panel'],
    include_package_data=True,
    url='https://github.com/hungluongkong/django2.0-debug-panel',
    license='BSD',
    description='django-debug-toolbar in WebKit DevTools. Works fine with background Ajax requests and non-HTML responses',
    long_description=open('README.rst').read(),
    install_requires=[
        "django-debug-toolbar >= 1.0"
    ],
)
