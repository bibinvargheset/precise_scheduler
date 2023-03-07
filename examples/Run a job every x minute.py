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
