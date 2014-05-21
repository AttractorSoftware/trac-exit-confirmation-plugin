# -*- coding: utf-8 -*-
from setuptools import setup

PACKAGE = 'TracExitConfirmation'
VERSION = '0.1'

setup(
    name=PACKAGE,
    version=VERSION,
    description='Trac Plugins',
    packages=['main'],
    entry_points = {'trac.plugins': [
        'main.trac_exit_confirmation = main.trac_exit_confirmation'
    ]},
    package_data={
    'main': ['htdocs/*.js']},
    install_requires=['trac']
)
