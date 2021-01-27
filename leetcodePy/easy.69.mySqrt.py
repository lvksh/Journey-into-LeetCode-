实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 思路
# sqrt(x) = a
# 因为 0 < a < x
# 从 x/2 开始二分搜索，直到搜索区域的两端的整数部分一致


class Solution:
    def mySqrt(x: int):
        p = 0
        q = x
        while(int(p) != int(q)):
            a = (p + q)/2.0 # 确定中点
            if a**2 == x:
                return(int(a))
            elif a**2 < x:
                p = a
            else:
                q = a
        return int(a)
                
                
# 牛顿法
def f(a, x):
    return a**2 - x

def df(a):
    return 2*a

def mySqrt(x: int):
    if x:
        List = [x/2.0]
    else:
        return 0
    List.append(List[-1] - f(List[-1],x)/df(List[-1],x))
    while int(List[-1]) != int(List[-2]):
        List.append(List[-1] - f(List[-1],x)/df(List[-1],x))
    return int(List[-1])
    
    
                