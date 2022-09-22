import io
from contextlib import redirect_stdout
from time import time


def timer_func(func):
    def wrappper(*args, **kwargs):
        wrappper.counter+=1
        start = time()
        # Perhaps, it's useful to use contextlib for redirect stdout here, because if your test function contains print() 
        # it will be printed to console, but we don't want it
        with redirect_stdout(io.StringIO) as output:
            result = func(*args, **kwargs)
        end = time()
        print(f'Function {func.__name__!r} execution time = {(end-start):.10f}s','called = ',wrappper.counter)
        return result
    wrappper.counter=0
    return wrappper

