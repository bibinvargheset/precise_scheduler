Installation
============


Python version support
######################

We recommend using the latest version of Python.
precise_scheduler is tested on Python 3.7, 3.8 and 3.9,3.10,3.11




Dependencies
############

precise_scheduler has no dependencies. None. Zero. Nada. Nopes.
We plan to keep it that way.


Installation instructions
#########################

Problems? Check out :doc:`faq`.

PIP (preferred)
***************
The recommended way to install this package is to use pip.
Use the following command to install it:

.. code-block:: bash

    $ pip install precise_scheduler

precise_scheduler is now installed.
Check out the :doc:`examples </examples>` or go to the :doc:`the documentation overview </index>`.



Install manually
**************************
If you don't have access to a package manager or need more control, you can manually copy the library into your project.
This is easy as the schedule library consists of a single sourcefile MIT licenced.
However, this method is highly discouraged as you won't receive automatic updates.

1. Go to the `Github repo <https://github.com/bibinvargheset/precise_scheduler`_.
2. Open file `schedule/__init__.py` and copy the code.
3. In your project, create a packaged named `schedule` and paste the code in a file named `__init__.py`.