import inspect
from time import time
 
def timer_func(func):
    def wrappper(*args, **kwargs):
        wrappper.counter+=1
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Function {func.__name__!r} execution time = {(end-start):.10f}s','called = ',wrappper.counter)
        print(f'Source code:\n{inspect.getsource(func)}')
        print('Docs :','\n', inspect.getdoc(func))
        return result
    wrappper.counter=0
    return wrappper