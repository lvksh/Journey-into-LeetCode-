假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

# 经典动态规划
# 思路一开始用递归
# 但是会造成许多重复的计算，例如clim(3) 会在计算clim(4)的时候被计算了两次
# 因此建立一个哈希表存储已经计算过的函数值，大大减少了时间

known = {0:0, 1:1, 2:2}

class Solution:
    def climbStairs(self, n: int):
        if n in known: return known[n]
        else:
            res = self.climbStairs(n-1) + self.climbStairs(n-2)
            known[n] = res
        return res