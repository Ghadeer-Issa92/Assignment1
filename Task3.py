import inspect
import io
from time import time
from contextlib import redirect_stdout 


class timer_func:
    global ranking
    ranking={} 
    
    # with redirect_stdout(io.StringIO()) as f:
    def __init__(self, func):
        self.function = func
        self.counter = 0
        self.time = 0.0
    def __call__(self, *args, **kwargs):
        with redirect_stdout(io.StringIO()) as output:
            start = time()
            result = self.function(*args, **kwargs)
            end= time()
            self.time = end-start
            self.counter += 1
            with open('log.txt', 'a+') as log:
                log.write(f'Function {self.function.__name__!r} execution time = {(self.time):.10f}s  called = {self.counter}\n')
                log.write(f'Name:\t\t{self.function.__name__}\n')
                log.write(f'Type:\t\t{type(self.function)}\n')
                log.write(f'sign :\t\t{inspect.signature(self.function)}\n')
                log.write(f'pos_Arg :\t{args}\n')
                log.write(f'kw_Arg :\t{kwargs}\n')
                # You can split getsource by '\n' and print each line with the same indentation.
                log.write(f'Source code:{inspect.getsource(self.function)}\n')
                # You can split getdoc by '\n' and print each line with the same indentation.
                log.write(f'Docs :\t\t{inspect.getdoc(self.function)}\n')
                log.write(f'Output:\t{output.getvalue()}\n\n')
                
        return result



