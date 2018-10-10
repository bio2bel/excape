Bio2BEL ExCAPE-DB |build|
=========================
Convert curated assays from ExCAPE-DB to BEL.

Installation |pypi_version| |python_versions| |pypi_license|
------------------------------------------------------------
``bio2bel_excape`` can be installed easily from `PyPI <https://pypi.python.org/pypi/bio2bel_excape>`_ with
the following code in your favorite terminal:

.. code-block:: sh

    $ python3 -m pip install bio2bel_excape

or from the latest code on `GitHub <https://github.com/bio2bel/excape>`_ with:

.. code-block:: sh

    $ python3 -m pip install git+https://github.com/bio2bel/excape.git

Setup
-----
Python REPL
~~~~~~~~~~~
.. code-block:: python

    >>> import bio2bel_excape
    >>> excape_manager = bio2bel_excape.Manager()
    >>> excape_manager.populate()

Command Line Utility
~~~~~~~~~~~~~~~~~~~~
.. code-block:: bash

    bio2bel_excape populate

Tests
-----
Bio2BEL ExCAPE uses `tox` for testing. After cloning the repository,
install `tox` with:

.. code-block:: sh

    $ python3 -m pip install tox

And run it in the base directory (the one that contains `tox.ini`) with:

.. code-block:: sh

    $ tox

References
----------
- Sun, J., *et al*. (2017). `ExCAPE-DB: An integrated large scale dataset facilitating Big Data analysis in
  chemogenomics <https://doi.org/10.1186/s13321-017-0203-5>`_. Journal of Cheminformatics, 9(1), 1–9.
- https://zenodo.org/record/173258/files/pubchem.chembl.dataset4publication_inchi_smiles.tsv.xz?download=1

.. |build| image:: https://travis-ci.com/bio2bel/excape.svg?branch=master
    :target: https://travis-ci.com/bio2bel/excape

.. |coverage| image:: https://codecov.io/gh/bio2bel/excape/coverage.svg?branch=master
    :target: https://codecov.io/gh/bio2bel/excape?branch=master
    :alt: Coverage Status

.. |docs| image:: https://readthedocs.org/projects/bio2bel-excape/badge/?version=latest
    :target: https://bio2bel.readthedocs.io/projects/excape/en/latest/?badge=latest
    :alt: Documentation Status

.. |python_versions| image:: https://img.shields.io/pypi/pyversions/bio2bel_excape.svg
    :alt: Stable Supported Python Versions

.. |pypi_version| image:: https://img.shields.io/pypi/v/bio2bel_excape.svg
    :alt: Current version on PyPI

.. |pypi_license| image:: https://img.shields.io/pypi/l/bio2bel_excape.svg
    :alt: MIT License
