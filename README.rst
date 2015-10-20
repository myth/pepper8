pepper8 |requirements| |version|
================================

Transform pep8 or flake8 output to HTML
---------------------------------------

To install pepper8, simply use pip.

.. code:: bash

    pip install pepper8


Or you can clone the latest master branch and build using setuptools

.. code:: bash

    git clone git@github.com:myth/pepper8.git && python setup.py install


Usage
-----

pepper8 operates in two different input modes and two different output modes.
To read pep8 / flake8 status reports from file use

.. code:: bash

    pepper8 -o report.html <filename>


If no output file is specified with ``-o``, the HTML report is written to stdout, allowing
output redirection or piping

.. code:: bash

    pepper8 <filename> | grep W301 > report.html


Build statistics
----------------

When pepper8 is run using an output file ``-o <filename>``, it will check its run environment
and print out available build statistics to stdout.

Currently, only TeamCity build statistics are supported with keys ``pepper8warnings`` and ``pepper8errors``.

If you wish to enable full parsing of all PEP 8 / Flake8 errors as failures in TeamCity,
there already exists a package called `TeamCity-messages <https://github.com/JetBrains/teamcity-messages>`_
which will be treated as build errors in TeamCity.

The TeamCity build statistics provided by pepper8 is only intended to provide statistical data for use in
custom build report graphs in addition to the HTML report.


.. |requirements| image:: https://requires.io/github/myth/pepper8/requirements.png?branch=master
    :target: https://requires.io/github/myth/requirements/?branch=master
    :alt: Requirements Status
.. |version| image:: https://pypip.in/py_versions/pepper8/badge.svg
    :target: https://pypi.python.org/pypi/pepper8/
    :alt: Latest Version
