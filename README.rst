..


Introduction
============

Build ``zipapp`` single file Python applications easily.


Repositories
------------

Binary distributions:

* https://pypi.org/project/zapp/

Source code:

* https://gitlab.com/sinoroc/zapp
* https://github.com/sinoroc/zapp


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

* `shiv`_
* `pex`_
* `superzippy`_


.. Links

.. _`shiv`: https://pypi.org/project/shiv/
.. _`pex`: https://pypi.org/project/pex/
.. _`superzippy`: https://pypi.org/project/superzippy/


.. EOF
