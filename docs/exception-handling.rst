Exception Handling
##################

precise_scheduler doesn't catch exceptions that happen during job execution. Therefore any exceptions thrown during job execution will bubble up and interrupt precise_scheduler's run_xyz function.

If you want to guard against exceptions you can wrap your job function
in a decorator like this:

.. code-block:: python

    import functools

    def catch_exceptions(cancel_on_failure=False):
        def catch_exceptions_decorator(job_func):
            @functools.wraps(job_func)
            def wrapper(*args, **kwargs):
                try:
                    return job_func(*args, **kwargs)
                except:
                    import traceback
                    print(traceback.format_exc())
                    if cancel_on_failure:
                        return precise_scheduler.CancelJob
            return wrapper
        return catch_exceptions_decorator

    @catch_exceptions(cancel_on_failure=True)
    def bad_task():
        return 1 / 0

    precise_scheduler.every(5).minutes.do(bad_task)

Another option would be to subclass precise_scheduler like @mplewis did in `this example <https://gist.github.com/mplewis/8483f1c24f2d6259aef6>`_.