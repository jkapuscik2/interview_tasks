# You have create a debbuging decorator that show name, result and arguments to called function
# All the calculation in your cool fibonnaci function works fine, but you found some weird behavior
# Explain why it happened and what can you do about it


def trace(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        print('%s(%r, %r) -> %r' % (f.__name__, args, kwargs, result))
        return result

    return wrapper


@trace
def fibonacci(nth):
    # Calculating nth fibonacci number
    if nth in (0, 1):
        return nth
    else:
        return fibonacci(nth - 1) + fibonacci(nth - 2)


help(fibonacci)
print(fibonacci.__name__)
# Printed "wrapper" WHY?
# @TODO FIX IT

print(fibonacci(2))
