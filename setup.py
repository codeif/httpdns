#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='httpdns',
    version='0.1.0',
    description="Get host's IP by D+ of DNSPod.",
    long_description=read('README.rst'),
    author='codeif',
    author_email='me@codeif.com',
    url='http://github.com/codeif/httpdns',
    license='MIT',
    packages=find_packages(exclude=['tests']),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
