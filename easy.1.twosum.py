# two sum
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。


def twoSum(nums, target):
    for i in range(len(nums)):
        if nums[i] <= target:
            index1 = i
        else:
            continue
        index2 = -1    
        for k in range(i+1,len(nums)):
            if nums[i] + nums[k] == target:
                index2 = k
                list = [i, k]
                return list
            else:
                continue
        if index2 == -1:
            continue
        
nums = [3,2,4]
target = 6
twoSum(nums, target)

def two_sum(nums, target):
        size = len(nums)
        for i, m in enumerate(nums):print([i,m])
            j = i + 1
            while j < size:
                if target == (m + nums[j]):
                    return [i, j]
                else:
                    # print(i, j, m + _n, " didn't match!")
                    j += 1


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

