pepper8
=======

.. image:: https://img.shields.io/pypi/v/pepper8.svg
    :alt: Pepper8 Version
    :target: https://pypi.python.org/pypi/pepper8
    
.. image:: https://requires.io/github/myth/pepper8/requirements.svg?branch=master
     :target: https://requires.io/github/myth/pepper8/requirements/?branch=master
     :alt: Requirements Status

Transform pep8 or flake8 output to HTML
---------------------------------------

To install pepper8, simply use pip.

.. code:: bash

    pip install pepper8


Or you can clone the latest master branch and build using setuptools

.. code:: bash

    git clone git@github.com:myth/pepper8.git && cd pepper8 && python setup.py install


Usage
-----

pepper8 operates in two different input modes and two different output modes.
To read pep8 / flake8 status reports from file use

.. code:: bash

    pepper8 -o report.html <filename>


or you can pipe output from another file or process

.. code:: bash

    cat flake8.out | pepper8 > report.html


If no output file is specified with ``-o``, the HTML report is written to stdout, allowing
output redirection or piping

.. code:: bash

    pepper8 <filename> | less


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

Screenshots from TeamCity integration
-------------------------------------
Pepper8 PEP 8 HTML Report


.. image:: https://cloud.githubusercontent.com/assets/2415878/10596725/7a2d17a6-76e7-11e5-8630-3e8bd4803a30.png
    :alt: Pepper8 PEP 8 HTML Report
    :align: center


TeamCity custom chart data using custom buildStatistics messages if run under TeamCity


.. image:: https://cloud.githubusercontent.com/assets/2415878/10596726/7a2f43aa-76e7-11e5-8833-429197b45025.png
    :alt: Custom TeamCity Flake8/PEP8 Warning/Error build metrics
    :align: center
    
=========
Changelog
=========

1.1.0
-----
Expand pepper8 to account for all possible alphanumeric
violation codes on a [A-Z][0-9]{3,4} format.
Updated broken link to flake8-readthedocs.

1.0.4
-----
Fixed a Python 2 and 3 compatibility issue.
Added changelog to README.

1.0.3
-----
Fixed a bug causing missed statistics for last file.
Split the title summary stats into the Flake8 plugins.

1.0.2
-----
Changed links in HTML report to default to new window.
This prevents TeamCity to display blank page due to
loading of "unsafe scripts" inside the iframe.


1.0.1
-----
A few bugfixes


1.0.0
-----

Initial release

