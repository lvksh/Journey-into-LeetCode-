# 思路
# 先转化成10尽职
import numpy as np
def twoToTen(a):
    # a is a str here
    aList = list(a)
    sumOfTen = sum([int(aList[-i-1]) * 2**i for i in range(len(aList))])
    return(sumOfTen)
 
def tenToTwo(a):
    # a is a int
    if a == 0:return(0);
    if a == 1:return(1);
    p = None
    q = []
    while p!=1:
        q.append(a % 2)
        a = p = a//2  
    q = q + [1]
    q.reverse()
    value = sum([q[-i-1] * 10**i for i in range(len(q))])
    return(value)
    
   

    def addBinary(a: str, b: str):
        sumOfTen = twoToTen(a) + twoToTen(b)
        return(tenToTwo(sumOfTen))
        
            

        
    
