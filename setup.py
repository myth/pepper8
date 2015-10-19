# -*- coding: utf-8

import os
import sys

__version__ = '0.1.0'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
with open('README.rst', encoding='utf-8') as r:
    readme = r.read()

# Dependencies
requires = [
    'Jinja2>=2.7',
]

setup(
    name='pepper8',
    version=__version__,
    description='Transforms pep8 or flake8 output into an HTML report.',
    long_description=r,
    author="Aleksander 'myth' Skraastad'",
    author_email='myth@overflow.no',
    packages=['pepper8'],
    license='MIT License',
    install_requires=requires,
    url='https://github.com/myth/pepper8',
    include_package_details=True,
    classifiers=[
        'Development status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Licence :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ]
)
