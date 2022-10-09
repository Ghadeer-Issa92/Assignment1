import math
from time import sleep
import Task1 
import Task2
import Task3
@Task3.timer_func
def quad(a,b,c):
    '''this function solves quadratic equation the input parameters is a, b, c '''
    if a == 0:
        print('incorrect input')
        return 0

    D=(b**2)-(4*a*c)
    if D>0:
        X1=(-b-math.sqrt(D))/(2*a)
        X2=(-b+math.sqrt(D))/(2*a)
        print ('X1= ', X1 ,' X2= ',X2)
    elif D==0:
        x1=x2=-b/(2*a)
        print ('X1=X2= ', -b/(2*a))
    else:
        x1=0
        print("Complex Roots") 
        print(- b / (2 * a), " + i", math.sqrt(abs(D))) 
        print(- b / (2 * a), " - i", math.sqrt(abs(D))) 

        
@Task3.timer_func
def pascal_triangle(n):
    '''this function print n lines of pascal triangle. the input is just n (number of rows to print) '''
    trow=[1]
    y=[0]
    
    for x in range(max(n,0)):
        print(" "*(n-x),end="")
        print (trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1

@Task3.timer_func
def sleeper(n):
    '''this function sleeps fo n seconds. the input is just n (number of seconds to sleep)  '''
    sleep(n)


if __name__ == '__main__':
    sleeper(2)
    pascal_triangle(6)
    quad(-22,4,-42)
    pascal_triangle(6)
    quad(-22,4,-42)
    sleeper(1)
