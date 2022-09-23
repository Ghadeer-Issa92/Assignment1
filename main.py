import math
from time import sleep
import Task1 
import Task2
import Task3
@Task1.timer_func
def quad(a,b,c):
    '''quad function docstring '''
    if a == 0:
        return 0

    D=(b**2)-(4*a*c)
    if D>0:
        X1=(-b-math.sqrt(D))/(2*a)
        X2=(-b+math.sqrt(D))/(2*a)
    elif D==0:
        x1=x2=-b/(2*a)
    else:
        x1=0
@Task1.timer_func
def pascal_triangle(n):
    '''pascal triangle doc string'''
    trow=[1]
    y=[0]
    
    for x in range(max(n,0)):
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1

@Task1.timer_func
def sleeper(n):
    '''this function don't need  docstring, but here is it anyway'''
    sleep(n)


if __name__ == '__main__':
    sleeper(2)
    pascal_triangle(6)
    quad(-22,4,-42)
    pascal_triangle(6)
    quad(-22,4,-42)
    sleeper(1)