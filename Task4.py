import inspect
import io
from time import time
from contextlib import redirect_stdout 


class timer_func:

    # with redirect_stdout(io.StringIO()) as f:
    def __init__(self, func):
        self.function = func
        self.counter = 0
        self.time = 0.0
    def __call__(self, *args, **kwargs):
        with redirect_stdout(io.StringIO()) as f:
            with open('Output.txt', 'a+') as Output:
                try:
                    start = time()
                    self.function(*args, **kwargs)
                    end= time()
                    self.time = end-start
                    self.counter += 1
                    
                    Output.write(f'Function {self.function.__name__!r} execution time = {(self.time):.10f}s  called = {self.counter}\n')
                    Output.write(f'Name:\t\t{self.function.__name__}\n')
                    Output.write(f'Type:\t\t{type(self.function)}\n')
                    Output.write(f'sign :\t\t{inspect.signature(self.function)}\n')
                    Output.write(f'pos_Arg :\t{args}\n')
                    Output.write(f'kw_Arg :\t{kwargs}\n')
                    # You can split getsource by '\n' and print each line with the same indentation.
                    Output.write(f'Source code:{inspect.getsource(self.function)}\n')
                    # You can split getdoc by '\n' and print each line with the same indentation.
                    Output.write(f'Docs :\t\t{inspect.getdoc(self.function)}\n')
                    Output.write(f'Output:\t{f.getvalue()}\n\n')
                except Exception as err:                                 
                    with open('log.log', 'a+') as log:  
                        log.write("RuntimeError : {0}\n".format(err))
                        return self.function
        return self.function



