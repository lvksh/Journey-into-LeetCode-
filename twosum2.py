# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，
# 并且它们的每个节点只能存储 一位 数字。

# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

# 示例：

# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        
def generateList(l: list) -> ListNode:
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next

def printList(l: ListNode):
    while l:
        print("%d, " %(l.val), end = '')
        l = l.next
    print('')


l1 = generateList([1, 5, 8])
l2 = generateList([9, 1, 2, 9])
printList(l1)
printList(l2)



class Solution:
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        l = []
        flag = 0
        # 这里有个好神奇的地方，除了0以外的所有东西都是1，即使他是个奇怪的类
        while l1 or l2: 
            if l1==None: l1 = ListNode(0)
            if l2==None: l2 = ListNode(0)
            val = l1.val + l2.val + 1 if flag else l1.val + l2.val
            flag = 1 if val >= 10 else 0
            if flag:
                left = val - 10
                l.append(left)
            else:
                l.append(val)
            l1 = l1.next
            l2 = l2.next
        return generateList(l)        
            
            
[1,8]
[0]
l2 = generateList([0])
l1 = generateList([1,8])

printList(Solution.addTwoNumbers(l1, l2))
