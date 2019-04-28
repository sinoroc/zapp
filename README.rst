..


Introduction
============

Build ``zipapp`` single file Python applications easily.


Usage
=====

Standalone application
----------------------

.. code::

    zapp myapp.pyz myapp.core:main myapp


Setuptools command
------------------

.. code::

    python3 setup.py bdist_zapp --entry-point myapp.core:main


Details
=======

Similar applications
--------------------

* Shiv https://shiv.readthedocs.io

* Pex https://pex.readthedocs.io


Hacking
=======

This project makes extensive use of `tox`_, `pytest`_, and `GNU Make`_.


Development environment
-----------------------

Use following command to create a Python virtual environment with all
necessary dependencies::

    tox --recreate -e develop

This creates a Python virtual environment in the ``.tox/develop`` directory. It
can be activated with the following command::

    . .tox/develop/bin/activate


Run test suite
--------------

In a Python virtual environment run the following command::

    make review

Outside of a Python virtual environment run the following command::

    tox --recreate


Build and package
-----------------

In a Python virtual environment run the following command::

    make package

Outside of a Python virtual environment run the following command::

    tox --recreate -e package


.. Links

.. _`GNU Make`: https://www.gnu.org/software/make/
.. _`pytest`: https://pytest.org/
.. _`tox`: https://tox.readthedocs.io/


.. EOF