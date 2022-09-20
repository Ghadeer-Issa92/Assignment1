import inspect
import io
from time import time
from contextlib import redirect_stdout 
class timer_func:
    global  log  
    global ranking
    ranking={} 
    log = open("log.txt","a+")# append mode
    # with redirect_stdout(io.StringIO()) as f:
    def __init__(self, func):
        self.function = func
        self.counter = 0
        self.time = 0.0
    def __call__(self, *args, **kwargs):
        with redirect_stdout(io.StringIO()):
            with open('log.txt', 'a+') as log:
                start = time()
                result = self.function(*args, **kwargs)
                end= time()
                self.time = end-start
                self.counter += 1
                log.write("Execution took {} seconds".format(self.time))
                log.write('{} is running for the {} time'.format(self.function.__name__ , self.counter))
                log.write(f'Function {self.function.__name__!r} execution time = {(end-start):.10f}s  called = {self.counter}')
                log.write(f'Source code:\n{inspect.getsource(self.function)}')
                log.write(f'Docs :\n {inspect.getdoc(self.function)}')
                log.close()
        return result



