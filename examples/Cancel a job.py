import precise_scheduler


def some_task():
    print("Hello world")


job = precise_scheduler.every().day.at("22:30").do(some_task)
print(precise_scheduler.jobs)
precise_scheduler.cancel_job(job)
print(precise_scheduler.jobs)
