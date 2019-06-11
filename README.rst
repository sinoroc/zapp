..


Introduction
============

Build ``zipapp`` single file Python applications easily.


Usage
=====

Standalone application
----------------------

.. code::

    zapp ~/bin/myapp myapp.cli:main 'myapp==1.2.3' 'mylib==3.2.1'

    python3 -m zapp ~/bin/myapp myapp.cli:main 'myapp==1.2.3' 'mylib==3.2.1'

    zapp toolmaker.pyz toolmaker.cli:main toolmaker
    zapp pipdeptree.pyz pipdeptree:main pipdeptree
    zapp ~/bin/httpie httpie.__main__:main httpie

    # Without requirements
    zapp zipfile.pyz zipfile:main


Library
-------

.. code::

    import zapp

    zapp.core.build_zapp(
        [
            'myapp==1.2.3',
            'mylib==3.2.1',
        ],
        'myapp.cli:main',
        'myapp.pyz',
    )


Setuptools command
------------------

.. code::

    python3 setup.py bdist_zapp --entry-point myapp.cli:main


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
