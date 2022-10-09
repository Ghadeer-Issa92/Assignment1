from time import time
import inspect
import io
import contextlib

func_list = {}
class timer_func:
    def __init__(self,func):
        self.func = func
        timer_func.count = 0
    def __call__(self,*args,**kwargs):
        timer_func.count += 1
        self.arguments = args
        start = time()
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.func(*args, **kwargs)
        end= time()
        exec_time = end - start
        global fun_list
        with open('log.txt', 'a+') as log:
            log.writelines(self.func.__name__ + " call" + str(timer_func.count)+ " executed in "+ str(exec_time)+ " sec\n") 
            log.writelines(f"Name: {self.func.__name__}\n")
            log.writelines(f"Type: {type(self.func)}\n")
            log.writelines(f"Sign: {inspect.signature(self.func)}\n")
            log.writelines(f"Doc:  {self.func.__doc__}\n")
            log.writelines(f"Source:  {inspect.getsource(self.func)}\n")
            log.writelines(f"Output:{output.getvalue()}\n")
        func_list.append((self.func.__name__, exec_time))
        return self.func
