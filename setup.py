#! /usr/bin/env python

from setuptools import setup
import sigdispatch

setup(
    name='sigdispatch',
    version=sigdispatch.__version__,
    description='A simple events library.',
    author='Tyba',
    author_email='toni@tyba.com',
    url='http://github.com/Tyba/sigdispatch',
    packages=[
        'sigdispatch',
    ],
)
