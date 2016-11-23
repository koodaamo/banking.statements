===============================
banking.statements
===============================

.. image:: https://badge.fury.io/py/banking.statements.png
    :target: http://badge.fury.io/py/banking.statements

.. image:: https://travis-ci.org/petri/banking.statements.png?branch=master
        :target: https://travis-ci.org/petri/banking.statements


Parse and work with multiple banking statement files

* Free software: BSD license

Installation
------------

Important: This package uses the Python3 "__init__.py -less" namespace packages. Due to that,
for local install, make sure to use 'pip install .' rather than
'setup.py install'. Otherwise, at least at the time of writing this
(11/2016), Python namespace support can get confused if 'setup.py install' is
used with for example both 'banking.statements' and 'banking.statements.osuuspankki'.

Features
--------

* check statement files
* merge them
* search them
