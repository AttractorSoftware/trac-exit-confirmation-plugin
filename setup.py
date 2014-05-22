# -*- coding: utf-8 -*-
from setuptools import setup

PACKAGE = 'TracExitConfirmation'
VERSION = '0.1'

setup(
    name=PACKAGE,
    version=VERSION,
    description='Trac Plugins',
    packages=['exit_confirmation'],
    entry_points = {'trac.plugins': [
        'exit_confirmation.trac_exit_confirmation = exit_confirmation.trac_exit_confirmation'
    ]},
    package_data={
    'exit_confirmation': ['htdocs/*.js']},
    install_requires=['trac']
)
