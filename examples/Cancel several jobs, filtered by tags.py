import precise_scheduler


def greet(name):
    print("Hello {}".format(name))


precise_scheduler.every().day.do(greet, "Andrea").tag("daily-tasks", "friend")
precise_scheduler.every().hour.do(greet, "John").tag("hourly-tasks", "friend")
precise_scheduler.every().hour.do(greet, "Monica").tag("hourly-tasks", "customer")
precise_scheduler.every().day.do(greet, "Derek").tag("daily-tasks", "guest")
print(precise_scheduler.get_jobs())
precise_scheduler.clear("daily-tasks")
print(precise_scheduler.get_jobs())
# [Every 1 day do greet('Andrea') (last run: [never], next run: 2023-03-08 14:34:01), Every 1 hour do greet('John') (last run: [never], next run: 2023-03-07 15:34:01), Every 1 hour do greet('Monica') (last run: [never], next run: 2023-03-07 15:34:01), Every 1 day do greet('Derek') (last run: [never], next run: 2023-03-08 14:34:01)]
# [Every 1 hour do greet('John') (last run: [never], next run: 2023-03-07 15:34:01), Every 1 hour do greet('Monica') (last run: [never], next run: 2023-03-07 15:34:01)]
