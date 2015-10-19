# -*- coding: utf-8

import os
import sys

__version__ = '1.0.0'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

with open('README.md', encoding='utf-8') as r:
    readme = r.read()

setup(
    name='pepper8',
    version=__version__,
    description='Transforms pep8 output into an HTML report.',
    long_description=r,
    author="Aleksander 'myth' Skraastad'",
    author_email='myth@overflow.no',
    packages=['pepper8'],
    license='MIT License',
    url='https://github.com/myth/pepper8',
    classifiers=[
        'Development status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Licence :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
