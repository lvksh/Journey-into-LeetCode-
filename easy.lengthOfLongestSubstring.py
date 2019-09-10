# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:
# 输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

# 示例 2:
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

# 示例 3:
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
def deflist(s,pointer):
    l = []
    
    while(s[pointer] not in l):    
        l.append(s[pointer])
        pointer += 1
        if pointer == len(s):
            break
    return l, pointer
    
    
    
def lengthOfLongestSubstring(s):
    if len(s) == 0: return 0
    pointer = 0
    all_list = []
    while 1:
        l, pointer = deflist(s, pointer)
        if(pointer == len(s)):
            all_list.append(l)
            break
        # 这个需要再理解一下
        pointer = [i for i,v in enumerate(s[:pointer]) if v==s[pointer]][-1] + 1
        #pointer = s[:pointer].index(s[pointer]) + 1  # bug
        all_list.append(l)
    return max([len(sub_list) for sub_list in all_list]) 

lengthOfLongestSubstring(s)
s = " "
len(s)
