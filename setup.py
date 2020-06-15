# -*- coding: utf-8 -*-
'''Setup module'''

import os
from setuptools import setup

exec(open('zerto/_version.py').read())
try:
    import requests     # NOQA
except ImportError:
    import sys
    sys.stderr.write(
        "Either install requests module with a package manager "
        "or with easy_install or pip\n"
        "E.g. easy_install requests\n"
    )


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='Zerto',
    version=__version__,
    description='Module for calling the Zerto api',
    author='Justin Paul',
    author_email='justin@jpaul.me',
    url='https://github.com/recklessop/pyzerto3',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: Apache Software License',
    ],
    packages=['zerto'],
    # install_requires=['requests'] # if not a recent python version
)

# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
