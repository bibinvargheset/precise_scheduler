import pause

from precise_scheduler import every, repeat, run_pending, default_scheduler
import time


@repeat(every(10).seconds)
def job():
    print("I am a scheduled job")


while True:
    pause.until(default_scheduler.get_next_run())
    run_pending()
