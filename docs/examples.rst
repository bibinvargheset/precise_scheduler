Examples
========

Eager to get started? This page gives a good introduction to Schedule.
It assumes you already have Schedule installed. If you do not, head over to :doc:`installation`.

Run a job every x minute
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

        import pause

        import precise_scheduler
        import time


        def job():
            print("I'm working...")


        # Run job every 3 second/minute/hour/day/week,
        # Starting 3 second/minute/hour/day/week from now
        precise_scheduler.every(3).seconds.do(job)
        precise_scheduler.every(3).minutes.do(job)
        precise_scheduler.every(3).hours.do(job)
        precise_scheduler.every(3).days.do(job)
        precise_scheduler.every(3).weeks.do(job)

        # Run job every minute at the 23rd second
        precise_scheduler.every().minute.at(":23").do(job)

        # Run job every hour at the 42rd minute
        precise_scheduler.every().hour.at(":42").do(job)

        # Run jobs every 5th hour, 20 minutes and 30 seconds in.
        # If current time is 02:00, first execution is at 06:20:30
        precise_scheduler.every(5).hours.at("20:30").do(job)

        # Run job every day at specific HH:MM and next HH:MM:SS
        precise_scheduler.every().day.at("10:30").do(job)
        precise_scheduler.every().day.at("10:30:42").do(job)
        precise_scheduler.every().day.at("12:42", "Europe/Amsterdam").do(job)

        # Run job on a specific day of the week
        precise_scheduler.every().monday.do(job)
        precise_scheduler.every().wednesday.at("13:15").do(job)
        precise_scheduler.every().minute.at(":17").do(job)

        while True:
            pause.until(precise_scheduler.default_scheduler.get_next_run())
            precise_scheduler.run_pending()

Use a decorator to schedule a job
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use the ``@repeat`` to schedule a function.
Pass it an interval using the same syntax as above while omitting the ``.do()``.

.. code-block:: python

        import pause

        from precise_scheduler import every, repeat, run_pending, default_scheduler
        import time


        @repeat(every(10).seconds)
        def job():
            print("I am a scheduled job")


        while True:
            pause.until(default_scheduler.get_next_run())
            run_pending()

The ``@repeat`` decorator does not work on non-static class methods.

Pass arguments to a job
~~~~~~~~~~~~~~~~~~~~~~~

``do()`` passes extra arguments to the job function

.. code-block:: python

    import precise_scheduler

    def greet(name):
        print('Hello', name)

    precise_scheduler.every(2).seconds.do(greet, name='Alice')
    precise_scheduler.every(4).seconds.do(greet, name='Bob')

    from precise_scheduler import every, repeat

    @repeat(every().second, "World")
    @repeat(every().day, "Mars")
    def hello(planet):
        print("Hello", planet)


Cancel a job
~~~~~~~~~~~~
To remove a job from the scheduler, use the ``precise_scheduler.cancel_job(job)`` method

.. code-block:: python

        import precise_scheduler


        def some_task():
            print("Hello world")


        job = precise_scheduler.every().day.at("22:30").do(some_task)
        print(precise_scheduler.jobs)
        precise_scheduler.cancel_job(job)
        print(precise_scheduler.jobs)

Run a job once
~~~~~~~~~~~~~~

Return ``precise_scheduler.CancelJob`` from a job to remove it from the scheduler.

.. code-block:: python

        import datetime

        import pause

        import precise_scheduler
        import time


        def job_that_executes_once():
            # Do some work that only needs to happen once...
            return precise_scheduler.CancelJob


        precise_scheduler.every().day.at("14:08").do(job_that_executes_once)


        pause.until(precise_scheduler.default_scheduler.get_next_run())
        print(precise_scheduler.default_scheduler.get_jobs(), datetime.datetime.now())
        precise_scheduler.run_pending()
        print(precise_scheduler.default_scheduler.get_jobs())

        # [Every 1 day at 14:08:00 do job_that_executes_once() (last run: [never], next run: 2023-03-07 14:08:00)] 2023-03-07 14:08:00.000091
        # []

Get all jobs
~~~~~~~~~~~~
To retrieve all jobs from the scheduler, use ``precise_scheduler.get_jobs()``

.. code-block:: python

    import precise_scheduler

    def hello():
        print('Hello world')

    precise_scheduler.every().second.do(hello)

    all_jobs = precise_scheduler.get_jobs()


Cancel all jobs
~~~~~~~~~~~~~~~
To remove all jobs from the scheduler, use ``precise_scheduler.clear()``

.. code-block:: python

        import precise_scheduler


        def greet(name):
            print("Hello {}".format(name))


        precise_scheduler.every().second.do(greet, name="Harry")
        precise_scheduler.every(2).seconds.do(greet, name="Alice")
        precise_scheduler.every().minute.do(greet, name="Bob")
        precise_scheduler.every().hour.do(greet, name="Sam")
        precise_scheduler.run_all()
        print(precise_scheduler.default_scheduler.get_jobs())
        precise_scheduler.clear()
        print(precise_scheduler.default_scheduler.get_jobs())

        # Hello Harry
        # Hello Alice
        # Hello Bob
        # Hello Sam
        # [Every 1 second do greet(name='Harry') (last run: 2023-03-07 14:12:51, next run: 2023-03-07 14:12:52), Every 2 seconds do greet(name='Alice') (last run: 2023-03-07 14:12:51, next run: 2023-03-07 14:12:53), Every 1 minute do greet(name='Bob') (last run: 2023-03-07 14:12:51, next run: 2023-03-07 14:13:51), Every 1 hour do greet(name='Sam') (last run: 2023-03-07 14:12:51, next run: 2023-03-07 15:12:51)]
        # []


Cancel several jobs, filtered by tags
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can cancel the scheduling of a group of jobs selecting them by a unique identifier.

.. code-block:: python

    import precise_scheduler

    def greet(name):
        print('Hello {}'.format(name))

    precise_scheduler.every().day.do(greet, 'Andrea').tag('daily-tasks', 'friend')
    precise_scheduler.every().hour.do(greet, 'John').tag('hourly-tasks', 'friend')
    precise_scheduler.every().hour.do(greet, 'Monica').tag('hourly-tasks', 'customer')
    precise_scheduler.every().day.do(greet, 'Derek').tag('daily-tasks', 'guest')

    print(precise_scheduler.get_jobs())
    precise_scheduler.clear("daily-tasks")
    print(precise_scheduler.get_jobs())
    # [Every 1 day do greet('Andrea') (last run: [never], next run: 2023-03-08 14:34:01), Every 1 hour do greet('John') (last run: [never], next run: 2023-03-07 15:34:01), Every 1 hour do greet('Monica') (last run: [never], next run: 2023-03-07 15:34:01), Every 1 day do greet('Derek') (last run: [never], next run: 2023-03-08 14:34:01)]
    # [Every 1 hour do greet('John') (last run: [never], next run: 2023-03-07 15:34:01), Every 1 hour do greet('Monica') (last run: [never], next run: 2023-03-07 15:34:01)]

    Will prevent every job tagged as ``daily-tasks`` from running again.


Run a job at random intervals
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    def my_job():
        print('Foo')

    # Run every 5 to 10 seconds.
    precise_scheduler.every(5).to(10).seconds.do(my_job)

``every(A).to(B).seconds`` executes the job function every N seconds such that A <= N <= B.


Run a job until a certain time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

    import precise_scheduler
    from datetime import datetime, timedelta, time

    def job():
        print('Boo')

    # run job until a 18:30 today
    precise_scheduler.every(1).hours.until("18:30").do(job)

    # run job until a 2030-01-01 18:33 today
    precise_scheduler.every(1).hours.until("2030-01-01 18:33").do(job)

    # precise_scheduler a job to run for the next 8 hours
    precise_scheduler.every(1).hours.until(timedelta(hours=8)).do(job)

    # Run my_job until today 11:33:42
    precise_scheduler.every(1).hours.until(time(11, 33, 42)).do(job)

    # run job until a specific datetime
    precise_scheduler.every(1).hours.until(datetime(2020, 5, 17, 11, 36, 20)).do(job)

The ``until`` method sets the jobs deadline. The job will not run after the deadline.

Time until the next execution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Use ``precise_scheduler.idle_seconds()`` to get the number of seconds until the next job is scheduled to run.
The returned value is negative if the next scheduled jobs was scheduled to run in the past.
Returns ``None`` if no jobs are scheduled.

.. code-block:: python

    import precise_scheduler
    import time

    def job():
        print('Hello')

    precise_scheduler.every(5).seconds.do(job)

    while 1:
        n = precise_scheduler.idle_seconds()
        if n is None:
            # no more jobs
            break
        elif n > 0:
            # sleep exactly the right amount of time
            time.sleep(n)
        precise_scheduler.run_pending()


Run all jobs now, regardless of their scheduling
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To run all jobs regardless if they are scheduled to run or not, use ``precise_scheduler.run_all()``.
Jobs are re-scheduled after finishing, just like they would if they were executed using ``run_pending()``.

.. code-block:: python

    import precise_scheduler

    def job_1():
        print('Foo')

    def job_2():
        print('Bar')

    precise_scheduler.every().monday.at("12:40").do(job_1)
    precise_scheduler.every().tuesday.at("16:40").do(job_2)

    precise_scheduler.run_all()

    # Add the delay_seconds argument to run the jobs with a number
    # of seconds delay in between.
    precise_scheduler.run_all(delay_seconds=10)