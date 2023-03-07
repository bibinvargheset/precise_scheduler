import pause

import precise_scheduler
import time


def greet(name):
    print("Hello", name)


precise_scheduler.every(2).seconds.do(greet, name="Alice")
precise_scheduler.every(4).seconds.do(greet, name="Bob")

from precise_scheduler import every, repeat


@repeat(every().second, "World")
@repeat(every().day, "Mars")
def hello(planet):
    print("Hello", planet)


while True:
    pause.until(precise_scheduler.default_scheduler.get_next_run())
    precise_scheduler.run_pending()
