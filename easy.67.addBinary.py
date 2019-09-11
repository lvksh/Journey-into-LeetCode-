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
    

# 题解
class Solution:
    def addBinary(self, a: str, b: str) :
        r, p = '', 0
        d = len(b) - len(a)
        a = '0' * d + a
        b = '0' * -d + b   
        # 先补齐位数
        for i, j in zip(a[::-1], b[::-1]): # 倒序遍历
            # p在这里表示进位 初始化是0
            s = int(i) + int(j) + p
            r = str(s % 2) + r
            p = s // 2
        return '1' + r if p else r

# 突然发现这个zip就是让你可以同时循环两个culmulator
# '0' * 负数 = ''
# 倒序遍历，r是存储最终结果的字符串，每一位相加后%2的结果存起来，所以如果加起来是2就变成0，加起来是3就变成1，
# p存储进位，如果s<2, p=0;如果s>=2, p=1
# 如果最终p==1，需要补一个1        
            

        
    
