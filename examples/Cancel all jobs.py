import precise_scheduler


def greet(name):
    print("Hello {}".format(name))


precise_scheduler.every().second.do(greet, name="Harry")
precise_scheduler.every(2).seconds.do(greet, name="Alice")
precise_scheduler.every().minute.do(greet, name="Bob")
precise_scheduler.every().hour.do(greet, name="Sam")
precise_scheduler.run_all()
print(precise_scheduler.default_scheduler.get_jobs())
precise_scheduler.clear()
print(precise_scheduler.default_scheduler.get_jobs())

# Hello Harry
# Hello Alice
# Hello Bob
# Hello Sam
# [Every 1 second do greet(name='Harry') (last run: 2023-03-07 14:12:51, next run: 2023-03-07 14:12:52), Every 2 seconds do greet(name='Alice') (last run: 2023-03-07 14:12:51, next run: 2023-03-07 14:12:53), Every 1 minute do greet(name='Bob') (last run: 2023-03-07 14:12:51, next run: 2023-03-07 14:13:51), Every 1 hour do greet(name='Sam') (last run: 2023-03-07 14:12:51, next run: 2023-03-07 15:12:51)]
# []
