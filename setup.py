# -*- coding: utf-8 -*-
from setuptools import setup

PACKAGE = 'TracExitConfirmation'
VERSION = '0.1'

setup(
    name=PACKAGE,
    version=VERSION,
    description='Web page exit confirmation plugin for Trac',
    author="IT Attractor",
    author_email="info@it-attractor.com",
    license='',
    url='',
    packages=['exit_confirmation'],
    entry_points = {'trac.plugins': [
        'exit_confirmation.trac_exit_confirmation = exit_confirmation.trac_exit_confirmation'
    ]},
    package_data={
    'exit_confirmation': ['htdocs/*.js']},
    install_requires=['trac']
)
