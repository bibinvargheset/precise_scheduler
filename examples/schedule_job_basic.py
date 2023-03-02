import datetime

import schedule
import time
import pause

scheduler = schedule.Scheduler()


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

# Hello Alice 2023-03-02 12:18:49.000329
# Hello Bob 2023-03-02 12:18:51.000153
# Hello Alice 2023-03-02 12:18:52.001699
# Hello World 2023-03-02 12:18:53.003097
# Hello Alice 2023-03-02 12:18:55.000087
# Hello Bob 2023-03-02 12:18:56.001523
# Hello Alice 2023-03-02 12:18:58.000147
# Hello World 2023-03-02 12:18:59.001626
