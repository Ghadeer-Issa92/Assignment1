import contextlib
import inspect
import io
from time import time
 
def timer_func(func):
    def wrappper(*args, **kwargs):
        wrappper.counter+=1
        start = time()
        # Perhaps, it's more reasonable to use contextlib here, to not duplicate code of function call)
        f=io.StringIO()
        with contextlib.redirect_stdout(f):
            result = func(*args, **kwargs)
        end = time()
        print(f'Function {func.__name__!r} execution time = {(end-start):.10f}s','called = ',wrappper.counter)
        print(f'Name:\t\t{func.__name__}')
        print(f'Type:\t\t{type(func)}')
        print(f'sign :\t\t{inspect.signature(func)}')
        print(f'pos_Arg :\t{args}')
        print(f'kw_Arg :\t{kwargs}')
        
        # You can align your source code while printing to make output more beautiful)
        # You can split getsource by '\n' and print each line with the same indentation.
        print(f'Source code:\tt{inspect.getsource(func)}')
        
        # You can split getdoc by '\n' and print each line with the same indentation.
        print('Docs :\t\t', inspect.getdoc(func))
        
        s=f.getvalue()
        print('Output :\t\t', s)    
        
        return result
    wrappper.counter=0
    return wrappper