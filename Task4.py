import inspect
import io
from time import time
from contextlib import redirect_stdout 
class timer_func:
    global  log  
    global ranking
    ranking={} 
    log = open("log.txt","a+")# append mode
        def __init__(self, func):
        self.function = func
        self.counter = 0
        self.time = 0.0
    def __call__(self, *args, **kwargs):
        with redirect_stdout(io.StringIO()):
            with open('Output.txt', 'a+') as Output:
                start = time()
                try:
                    self.function(*args, **kwargs)
                    end= time()
                    self.time = end-start
                    self.counter += 1
                    Output.write("Execution took {} seconds".format(self.time))
                    Output.write('{} is running for the {} time'.format(self.function.__name__ , self.counter))
                    Output.write(f'Function {self.function.__name__!r} execution time = {(end-start):.10f}s  called = {self.counter}')
                    Output.write(f'Source code:\n{inspect.getsource(self.function)}')
                    Output.write(f'Docs :\n {inspect.getdoc(self.function)}')
                    Output.close()
                except ZeroDivisionError as err:
                  with redirect_stdout(io.StringIO()):
                     with open('log.log', 'a+') as log:  
                        log.write("RuntimeError : {0}".format(err))
                        return self.function
        return self.function



