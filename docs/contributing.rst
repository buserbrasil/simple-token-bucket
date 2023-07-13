Contributing
============

Welcome! First of all, thank you for your interest in contributing to
the project! :)

Do you known the `Hatch <https://hatch.pypa.io/latest/>`_ project? Most
of the technical pains in this project are solved using this tool.

Style
-----

We use black + ruff to lint the project. Run :code:`hatch run style` to check
for any errors before pushing a commit. Most of lint errors can be solved
with :code:`hatch run fmt`.	

Testing
-------

This project uses pytest. Always run :code:`hatch run test:cov` to make
sure you changes don't break anything.

Documentation
-------------

If you make changes to docs, you can preview the changes locally running::

	hatch run doc
	open _build/html/index.html
