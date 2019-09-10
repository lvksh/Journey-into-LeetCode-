给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

d = dict({'{':'}','(':')',"[":']'})

def find_the_right(s, pointer):
    left_l = []
    while s[pointer] in ['[', '(', '{']:
        left_l.append(s[pointer])
        pointer += 1
        if pointer >= len(s): return False, pointer
    #if len(left_l) == 0: return False, pointer
    right_l = list(map(d.get, left_l))
    right_l.reverse()
    right_l = "".join(right_l)
    return right_l == s[pointer : (pointer+len(right_l))], pointer + len(right_l) + 1

def isValid(s):
    if s == "": return 1;
    pointer = 0
    flag = 1
    while pointer < len(s) and flag:
        flag, pointer = find_the_right(s, pointer)
    if not flag: return False
    else: return True    

s = "["
isValid(s)

s = "()[]{}"
isValid(s)

s = "]"
isValid(s)

# 不行不行啊
# 要用栈来写

d = dict({'{':'}','(':')',"[":']'})
def isValid(s):
    if len(s) == 0:
        return False
    temp = []
    for pointer in s:
        if pointer in d:
            temp.append(pointer)
        else:
            left = temp.pop() if temp else '#'
            correct_right = d.get(left)
            if correct_right != pointer:
                return False
    return len(temp) == 0        

    