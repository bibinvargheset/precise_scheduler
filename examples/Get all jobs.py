import precise_scheduler


def hello():
    print("Hello world")


precise_scheduler.every().second.do(hello)

all_jobs = precise_scheduler.get_jobs()
print(all_jobs)
