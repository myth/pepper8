# -*- coding: utf-8

import os
import sys

__version__ = '1.0.3'

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
with open('README.rst') as r:
    readme = r.read()
with open('CHANGELOG.rst') as c:
    changelog = c.read()

# Dependencies
requires = [
    'Jinja2>=2.7',
]

setup(
    name='pepper8',
    version=__version__,
    description='Transforms pep8 or flake8 output into an HTML report.',
    long_description=readme + '\n\n' + changelog,
    author="Aleksander 'myth' Skraastad'",
    author_email='myth@overflow.no',
    packages=['pepper8'],
    license='MIT License',
    install_requires=requires,
    url='https://github.com/myth/pepper8',
    package_data={
        '': ['CHANGELOG.rst'],
        'pepper8': ['templates/*.html']
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    entry_points={
        'console_scripts': ['pepper8 = pepper8.pepper8:main']
    }
)
