编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: l = ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

def longestCommonPrefix(strs):
    window = [""]
    i = 0
    if len(strs) <= 1: return("".join(strs))
    if "" in strs: return("")
    while i < np.min([len(k) for k in strs]):
        s = set([str[i] for str in strs])
        if len(s) == 1:
            window.append(strs[0][i])
            i += 1
        else: 
            break
    result = "".join(window)
    return(result)     
        

其他解法
def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
    res = ""
    for tmp in zip(*strs):
        print(tmp)
        tmp_set = set(tmp)
        if len(tmp_set) == 1:
            res += tmp[0]
        else:
            break
    return res


import numpy as np


