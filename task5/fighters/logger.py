import time
from functools import wraps


class Debugger:
    DEBUG = True


def logged(time_format, name_prefix=""):
    def decorator(func):
        if hasattr(func, '_logged_decorator') and func._logged_decorator:
            return func

        @wraps(func)
        def decorated_func(*args, **kwargs):
            start_time = time.time()
            print("- Running '{}' on {} ".format(
                name_prefix + func.__name__,
                time.strftime(time_format)
            ))
            result = func(*args, **kwargs)
            end_time = time.time()
            print("- Finished '{}', execution time = {:0.3f}s ".format(
                name_prefix + func.__name__,
                end_time - start_time
            ))
            return result

        decorated_func._logged_decorator = True
        return decorated_func

    return decorator


# Теперь можно создать декоратор класса.
def log_method_calls(time_format):
    def decorator(cls):
        for o in dir(cls):
            if o.startswith('__'):
                continue
            a = getattr(cls, o)
            if hasattr(a, '__call__'):
                if Debugger.DEBUG:
                    decorated_a = logged(time_format, cls.__name__ + ".")(a)
                    setattr(cls, o, decorated_a)
        return cls

    return decorator