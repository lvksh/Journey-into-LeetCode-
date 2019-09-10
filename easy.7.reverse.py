# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

# 注意:
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2^31,  2^31 − 1]。请根据这个假设，
# 如果反转后整数溢出那么就返回 0。

# 大概思路就是先转换成一个list，然后分情况逆序遍历，这个有点很简单，不过想写的很高效也有点难。
# 下面是我自己的解法，里面
# list[::-1]是倒序遍历整个list 因为完整写法是list[start:end:step]
# "".join(list) 可以把list里面的东西join一起 神奇

def reverse(x):
    l = list(str(x))
    if l[0] == '-':
        l_rev = l[::-1] 
        l_rev.pop()
        l_str = "".join(l_rev)
        output = - int(l_str)
    else:
        l_rev = l[::-1] 
        l_str = "".join(l_rev)
        output = int(l_str)
    if output < 2**31 - 1 and output > -2**31: 
        return output
    else:
        return 0

# 现在试试另一个方法
# 就是储存每一位数然后乘出来
import numpy as np
def reverse2(x):
    flag = 1 if x<0 else 0
    if flag: x = -x
    len_x = len(str(x))
    digits = [x//(10**k) % 10 for k in range(len_x)]
    tens = [10**k for k in range(len_x)]
    output = np.dot(digits[::-1], tens)
    if output < 2**31 - 1 and output > -2**31: 
        if flag: return -output
        else: return output
    else:
        return 0
    
import datetime
starttime = datetime.datetime.now()
temp = [10**k for k in range(1000)]
endtime = datetime.datetime.now()
print (endtime - starttime)
 
starttime = datetime.datetime.now()
temp = [10**k for k in range(1000)]
endtime = datetime.datetime.now()
print (endtime - starttime) 
            
# [x//(10**k) % 10 for k in range(len(list(str(x))))]
            
# reverse(123)
# a = 123
# l = list(str(a))
# l[::-1]


def reverse3(x):
    l = list(str(x))
    if l[0] == '-':
        l_rev = list(reversed(l))
        l_rev.pop()
        l_str = "".join(l_rev)
        output = - int(l_str)
    else:
        l_rev = list(reversed(l)) 
        l_str = "".join(l_rev)
        output = int(l_str)
    if output < 2**31 - 1 and output > -2**31: 
        return output
    else:
        return 0