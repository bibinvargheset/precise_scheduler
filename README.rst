`Precise_scheduler <https://schedule.readthedocs.io/>`__
=========================================================


Python job scheduling for humans. Run Python functions (or any other callable) periodically using a friendly syntax.

- A simple to use API for scheduling jobs, made for humans.
- In-process scheduler for periodic jobs. No extra processes needed!
- Very lightweight and no external dependencies.
- Excellent test coverage.

Usage
-----

.. code-block:: bash

    $ pip install precise-scheduler

.. code-block:: python


    import datetime
    import precise_scheduler
    import time
    import pause

    scheduler = precise_scheduler.Scheduler(schedule_base="last_schedule")
    #scheduler = precise_scheduler.Scheduler(schedule_base="last_run_start")
    #scheduler = precise_scheduler.Scheduler()


    def greet(name):
        print("Hello", name, datetime.datetime.now())
        time.sleep(1)


    scheduler.every(2).seconds.do(greet, name="Alice")
    scheduler.every(4).seconds.do(greet, name="Bob")

    from precise_scheduler import every, repeat


    @repeat(scheduler.every(5).seconds, "World")
    @repeat(scheduler.every().day, "Mars")
    def hello(planet):
        print("Hello", planet, datetime.datetime.now())
        time.sleep(0.5)


    while True:
        pause.until(scheduler.get_next_run())
        scheduler.run_pending()

    # Hello Alice 2023-03-02 12:24:31.000249
    # Hello Alice 2023-03-02 12:24:33.000094
    # Hello Bob 2023-03-02 12:24:34.001463
    # Hello World 2023-03-02 12:24:35.003073
    # Hello Alice 2023-03-02 12:24:35.503961
    # Hello Alice 2023-03-02 12:24:37.000157
    # Hello Bob 2023-03-02 12:24:38.001703
    # Hello Alice 2023-03-02 12:24:39.003366
    # Hello World 2023-03-02 12:24:40.004778
    # Hello Alice 2023-03-02 12:24:41.000172


Background
----------

This package is a slight improvement of https://github.com/dbader/schedule

The changes are

- Previously the calculation of next schedule was based on end of execution. Now you can also select based on start of last execution start or based on schedule (will be same unless you have a on demand execution).

- All schedules will be truncated to 0 microseconds.

- The code is updated to newer Pep requirements

The  reason for starting this package is the above updates are really needed and the package has not being updated for long and is under MIT licence.

For now the documentation remains the same only difference is mentioned below in code example and you can check out examples folder for python files


Documentation
-------------

precise_scheduler's documentation lives at `precise_scheduler.readthedocs.io <https://precise_scheduler.readthedocs.io/>`_.


Meta
----

Bibin Varghese - `@bibinvargheset <https://twitter.com/bibinvargheset>`_ - bibinvargheset@gmail.com

This package is a based on https://github.com/dbader/schedule

Inspired by `Adam Wiggins' <https://github.com/adamwiggins>`_ article `"Rethinking Cron" <https://adam.herokuapp.com/past/2010/4/13/rethinking_cron/>`_ and the `clockwork <https://github.com/Rykian/clockwork>`_ Ruby module.

Distributed under the MIT license. See `LICENSE.txt <https://github.com/bibinvargheset/precise_scheduler/LICENSE.txt>`_ for more information.

https://github.com/bibinvargheset/precise_scheduler