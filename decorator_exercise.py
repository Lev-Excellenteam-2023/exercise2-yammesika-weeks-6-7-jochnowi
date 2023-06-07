from functools import wraps


def type_check(correct_type):
    def decorator(func):
        @wraps(func)
        def wrapper(arg):
            if not isinstance(arg, correct_type):
                raise TypeError(f"Argument {arg} does not match the expected type {correct_type}.")
            return func(arg)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(66))
print(times2(66.0))
