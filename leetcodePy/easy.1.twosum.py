# two sum
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。


def twoSum(nums, target):
  d = dict()
    for i,j in enumerate(nums):
      d[j] = i
    for i in nums:
      if j = d.get(target - nums[i]) is not None:
        return i,  j

two_sum(nums, target)

def two_sum(nums, target):
    _dict = {}
    for i, m in enumerate(nums):
        _dict[m] = i
    for i, m in enumerate(nums):
        #print([i,m])
        j = _dict.get(target - m)
        #print(j)
        if j is not None and i != j:
            return [i, j]



