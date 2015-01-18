# -*- coding: utf-8 -*-
"""Installer for the genweb.templates package."""

from setuptools import find_packages
from setuptools import setup

import os


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = \
    read('README.rst') + \
    read('docs', 'HISTORY.rst') + \
    read('docs', 'LICENSE.txt')

setup(
    name='genweb.templates',
    version='1.2.dev0',
    description="Templates for Genweb projects",
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='templates mr bob genweb',
    author='UPCnet Plone Team',
    author_email='plone.team@upcnet.es',
    url='http://pypi.python.org/pypi/genweb.templates',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['genweb'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    entry_points="""
    [z3c.autoinclude.plugin]
    target = plone
    """,
)
