Reference
=========

.. module:: precise_scheduler

This part of the documentation covers all the interfaces of schedule.

Main Interface
--------------

.. autodata:: default_scheduler
.. autodata:: jobs

.. autofunction:: every
.. autofunction:: run_pending
.. autofunction:: run_all
.. autofunction:: get_jobs
.. autofunction:: clear
.. autofunction:: cancel_job
.. autofunction:: next_run
.. autofunction:: idle_seconds


Classes
-------

.. autoclass:: precise_scheduler.Scheduler
   :members:
   :undoc-members:

.. autoclass:: precise_scheduler.Job
   :members:
   :undoc-members:


Exceptions
----------

.. autoexception:: precise_scheduler.CancelJob