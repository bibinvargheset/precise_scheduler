import precise_scheduler


def greet(name):
    print("Hello {}".format(name))


precise_scheduler.every().day.do(greet, "Andrea").tag("daily-tasks", "friend")
precise_scheduler.every().hour.do(greet, "John").tag("hourly-tasks", "friend")
precise_scheduler.every().hour.do(greet, "Monica").tag("hourly-tasks", "customer")
precise_scheduler.every().day.do(greet, "Derek").tag("daily-tasks", "guest")

friends = precise_scheduler.get_jobs("friend")
print(friends)
