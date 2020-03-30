..


Introduction
============

Build `zipapp`_ (`PEP 441`_) single file Python applications easily.


Repositories
------------

Distributions:

* https://pypi.org/project/zapp/

Source code:

* https://gitlab.com/sinoroc/zapp
* https://github.com/sinoroc/zapp


Usage
=====

Standalone application
----------------------

.. code::

    usage: zapp [-h] [--version] [--requirement requirements.txt]
                output_file entry_point [requirement [requirement ...]]

    positional arguments:
      output_file
      entry_point
      requirement

    optional arguments:
      -h, --help            show this help message and exit
      --version             show program's version number and exit
      --requirement requirements.txt, -r requirements.txt


.. code::

    zapp ~/bin/myapp myapp.cli:main 'myapp==1.2.3' 'mylib==3.2.1'
    zapp ~/bin/myapp myapp.cli:main --requirement requirements.txt

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
        'myapp.pyz',  # output_file
        'myapp.cli:main',  # entry_point
        requirements=[
            'myapp==1.2.3',
            'mylib==3.2.1',
        ],
        requirements_txt='requirements.txt',
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
.. _`PEP 441`: https://www.python.org/dev/peps/pep-0441/
.. _`superzippy`: https://pypi.org/project/superzippy/
.. _`zipapp`: https://docs.python.org/3/library/zipapp.html


.. EOF
