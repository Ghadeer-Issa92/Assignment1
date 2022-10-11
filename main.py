import math
from time import sleep

import Task1 
import Task2
import Task3
import Task4
@Task3.timer_func
def quad(a,b,c):
    '''quadratic equation solver (takes three parameters a,b,c. ax^2 + bx + c = 0) '''
    if a == 0:
        print('incorrect input')
        return 0
   
    D=(b**2)-(4*a*c)
    #uncomment the next line to raise an division by zeroRuntimeError =============
      # error = D/0
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
def pascal(n):
    '''pascal triangle doc string'''
    trow=[1]
    y=[0]
    
    for x in range(max(n,0)):
        print(" "*(n-x),end="")
        print (trow)
        trow=[l+r for l,r in zip(trow+y, y+trow)]
    return n>=1

@Task3.timer_func
def sleeper(n):
    '''this function don't need  docstring, but here is it anyway'''
    sleep(n)



if __name__ == '__main__':
    
    sleeper(2)
    pascal(6)
    quad(-22,4,-42)
    pascal(6)
    quad(-22,4,-42)
    sleeper(1)

   
    print("PROGRAM   ||  RANK  ||   TIME ELAPSED")
    Task3.func_list.sort(key=lambda x: x[1])

    j=1
    for key,val in Task3.func_list:
        print(f'{key}\t\t{j}\t{val:.4f} s')
        j+=1
