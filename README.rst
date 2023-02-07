======
cdtool
======


.. image:: https://img.shields.io/pypi/v/cdtool.svg
        :target: https://pypi.python.org/pypi/cdtool

.. image:: https://img.shields.io/travis/idekerlab/cdtool.svg
        :target: https://travis-ci.com/idekerlab/cdtool

.. image:: https://readthedocs.org/projects/cdtool/badge/?version=latest
        :target: https://cdtool.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




this is my project


* Free software: MIT license
* Documentation: https://cdtool.readthedocs.io.



Dependencies
------------

* TODO add

Compatibility
-------------

* Python 3.3+

Installation
------------

.. code-block::

   git clone https://github.com/idekerlab/cdtool
   cd cdtool
   make dist
   pip install dist/cdtoolcmd*whl


Run **make** command with no arguments to see other build/deploy options including creation of Docker image 

.. code-block::

   make

Output:

.. code-block::

   clean                remove all build, test, coverage and Python artifacts
   clean-build          remove build artifacts
   clean-pyc            remove Python file artifacts
   clean-test           remove test and coverage artifacts
   lint                 check style with flake8
   test                 run tests quickly with the default Python
   test-all             run tests on every Python version with tox
   coverage             check code coverage quickly with the default Python
   docs                 generate Sphinx HTML documentation, including API docs
   servedocs            compile the docs watching for changes
   testrelease          package and upload a TEST release
   release              package and upload a release
   dist                 builds source and wheel package
   install              install the package to the active Python's site-packages
   dockerbuild          build docker image and store in local repository
   dockerpush           push image to dockerhub




Needed files
------------

**TODO:** Add description of needed files


Usage
-----

For information invoke :code:`cdtoolcmd.py -h`

**Example usage**

**TODO:** Add information about example usage

.. code-block::

   cdtoolcmd.py # TODO Add other needed arguments here


Via Docker
~~~~~~~~~~~~~~~~~~~~~~

**Example usage**

**TODO:** Add information about example usage


.. code-block::

   docker run -v `pwd`:`pwd` -w `pwd` idekerlab/cdtool:0.1.0 cdtoolcmd.py # TODO Add other needed arguments here


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _NDEx: http://www.ndexbio.org
