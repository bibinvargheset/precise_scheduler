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
