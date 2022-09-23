from time import time
import contextlib
import io

def timer_func(func):
    def wrapper_f(*args, **kwargs):
        wrapper_f.calls +=1
        f = io.StringIO()
        start = time()
        with contextlib.redirect_stdout(f):
            func(*args, **kwargs)
        end = time()
        result = f.getvalue()
        print(f'{func.__name__} call {wrapper_f.calls} excuted in {(end-start):.4f} sec')
        return result
    wrapper_f.calls=0
    return wrapper_f

