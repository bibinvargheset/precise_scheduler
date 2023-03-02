import datetime

import schedule
import time
import pause

scheduler = schedule.Scheduler(schedule_base="last_run_start")


def greet(name):
    print("Hello", name, datetime.datetime.now())
    time.sleep(1)


scheduler.every(2).seconds.do(greet, name="Alice")
scheduler.every(4).seconds.do(greet, name="Bob")

from schedule import every, repeat


@repeat(scheduler.every(5).seconds, "World")
@repeat(scheduler.every().day, "Mars")
def hello(planet):
    print("Hello", planet, datetime.datetime.now())
    time.sleep(0.5)


while True:
    pause.until(scheduler.get_next_run())
    scheduler.run_pending()

# Hello Alice 2023-03-02 12:27:37.000269
# Hello Alice 2023-03-02 12:27:39.000132
# Hello Bob 2023-03-02 12:27:40.001676
# Hello World 2023-03-02 12:27:41.003253
# Hello Alice 2023-03-02 12:27:41.504158
# Hello Alice 2023-03-02 12:27:43.000161
# Hello Bob 2023-03-02 12:27:44.001589
