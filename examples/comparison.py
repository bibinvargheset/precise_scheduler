import datetime

import precise_scheduler
import time
import schedule

scheduler = precise_scheduler.Scheduler(schedule_base="last_schedule")
schedule_old = schedule.Scheduler()


def greet(name):
    print("Hello", name, datetime.datetime.now())
    time.sleep(1)


scheduler.every(3).seconds.do(greet, name="precise_scheduler")
schedule_old.every(3).seconds.do(greet, name="schedule")

greet("start of test")

while True:
    time.sleep(0.001)
    scheduler.run_pending()
    schedule_old.run_pending()

#
# Hello precise_scheduler 2023-03-08 11:16:42.000479
# Hello schedule 2023-03-08 11:16:43.001039
# Hello precise_scheduler 2023-03-08 11:16:45.000918
# Hello schedule 2023-03-08 11:16:47.002968
# Hello precise_scheduler 2023-03-08 11:16:48.004551
# Hello precise_scheduler 2023-03-08 11:16:51.000129
# Hello schedule 2023-03-08 11:16:52.001413
