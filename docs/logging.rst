Logging
=======

Schedule logs messages to the Python logger named ``schedule`` at ``DEBUG`` level.
To receive logs from Schedule, set the logging level to ``DEBUG``.

.. code-block:: python

    import precise_scheduler
    import logging

    logging.basicConfig()
    precise_scheduler_logger = logging.getLogger('precise_scheduler')
    precise_scheduler_logger.setLevel(level=logging.DEBUG)

    def job():
        print("Hello, Logs")

    precise_scheduler.every().second.do(job)

    precise_scheduler.run_all()

    precise_scheduler.clear()

This will result in the following log messages:

.. code-block:: text

    DEBUG:precise_scheduler:Running *all* 1 jobs with 0s delay in between
    DEBUG:precise_scheduler:Running job Job(interval=1, unit=seconds, do=job, args=(), kwargs={})
    Hello, Logs
    DEBUG:precise_scheduler:Deleting *all* jobs


Customize logging
-----------------
The easiest way to add reusable logging to jobs is to implement a decorator that handles logging.
As an example, below code adds the ``print_elapsed_time`` decorator:

.. code-block:: python

    import functools
    import time
    import precise_scheduler

    # This decorator can be applied to any job function to log the elapsed time of each job
    def print_elapsed_time(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_timestamp = time.time()
            print('LOG: Running job "%s"' % func.__name__)
            result = func(*args, **kwargs)
            print('LOG: Job "%s" completed in %d seconds' % (func.__name__, time.time() - start_timestamp))
            return result

        return wrapper


    @print_elapsed_time
    def job():
        print('Hello, Logs')
        time.sleep(5)

    precise_scheduler.every().second.do(job)

    precise_scheduler.run_all()

This outputs:

.. code-block:: text

    LOG: Running job "job"
    Hello, Logs
    LOG: Job "job" completed in 5 seconds