#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='banking.statements',
    version='0.1.0',
    description='Tool to parse and work with multiple banking statement files',
    long_description=readme + '\n\n' + history,
    author='Petri Savolainen',
    author_email='petri@koodaamo.fi',
    url='https://github.com/koodaamo/banking.statements',
    namespace_packages=["banking"],
    packages=["banking.statements"],
    include_package_data=True,
    install_requires=[
        "setuptools",
        "docopt",
        "ofxstatement",
    ],
    entry_points="""
       [console_scripts]
       statements = banking.statements.command:statements
    """,
    license="BSD",
    zip_safe=False,
    keywords='banking,ofx,ofxstatement',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests.test_suite',
)
