将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

思路：
有两个链表，l1和l2，
1.  先比较l1.val和l2.val
2.  如果一样大：一起记录，一起next
        如果不一样大：
        先记录小的那个，小的next，重复步骤1，2
        
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    
class Solution:
    def mergeTwoLists(l1, l2):
        preListNode = ListNode(0)
        lastListNode = preListNode
        while l1 and l2 :
            if l1.val == l2.val:
                lastListNode.next = ListNode(l1.val)
                lastListNode = lastListNode.next
                l1 = l1.next
                lastListNode.next = ListNode(l2.val)
                lastListNode = lastListNode.next
                l2 = l2.next
            elif l1.val < l2.val:
                lastListNode.next = ListNode(l1.val)
                lastListNode = lastListNode.next
                l1 = l1.next
            else:
                lastListNode.next = ListNode(l2.val)
                lastListNode = lastListNode.next
                l2 = l2.next
        
        if l1 == None:
            lastListNode.next = l2
        elif l2 == None:
            lastListNode.next = l1
        return preListNode.next
 
def generateList(l: list):
    prenode = ListNode(0)
    lastnode = prenode
    for val in l:
        lastnode.next = ListNode(val)
        lastnode = lastnode.next
    return prenode.next  

l1 = generateList([1,2,4])
l2 = generateList([1,3,4])
l = mergeTwoLists(l1, l2)             

# 修正一下思路
有两个链表，l1和l2，
1.  先比较l1.val和l2.val
2.  先记录小的那个，小的next，重复步骤1，2

class Solution:
    def mergeTwoLists(l1, l2):
        preListNode = ListNode(0)
        lastListNode = preListNode
        while l1 and l2 :
            if l1.val <= l2.val:
                lastListNode.next = ListNode(l1.val)
                l1 = l1.next
            else:
                lastListNode.next = ListNode(l2.val)
                l2 = l2.next
            lastListNode = lastListNode.next
            
        # if l1 == None:
        #     lastListNode.next = l2
        # elif l2 == None:
        #     lastListNode.next = l1
        lastListNode.next = l1 if l1 is not None else l2
        return preListNode.next
    
# 递归的做法

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

