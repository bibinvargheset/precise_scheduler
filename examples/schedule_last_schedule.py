import datetime

import precise_scheduler
import time
import pause

scheduler = precise_scheduler.Scheduler(schedule_base="last_schedule")


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