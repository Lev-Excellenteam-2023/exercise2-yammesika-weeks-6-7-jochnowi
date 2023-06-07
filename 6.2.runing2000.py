import time


def timer(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    return time.time() - start_time


print(timer(print, "Hello"))

print(timer(zip, [1, 2, 3], [4, 5, 6]))

print(timer("Hi {name}".format, name="Bug"))

print(timer(lambda a, b: a**b, 5555, 55589))


