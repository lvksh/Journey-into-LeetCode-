Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack): return -1
        if len(haystack) == 0: return 0
        i = 0
        while i < len(haystack):
            if haystack[i] != needle[0]: i=i+1
            else:
                ind = i 
                flag = True
                for item in needle:
                    if haystack[i]!=item:
                        flag = False
                        break
                    else:
                        i = i + 1
                if flag:
                    return ind
                else:
                    i = ind + 1
        return -1
                    
haystack = "a"
needle = "a"
q = Solution()
w = q.strStr(haystack, needle)
w