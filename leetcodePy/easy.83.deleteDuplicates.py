给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

known = {}
class Solution:
    def deleteDuplicates1(head: ListNode):
        pointer = ListNode(0)
        pointer.next = head
        preNode = pointer
        while pointer != None and pointer.next:
            if pointer.next.val not in known:
                known[pointer.next.val] = 1
                pointer = pointer.next
            else:
                pointer.next = pointer.next.next
                if pointer.next:
                    pointer = pointer.next 
        if pointer.val in known:
            pointer = None
        return preNode.next
    
head = ListNode(1)
deleteDuplicates(head).val

class Solution:
    def deleteDuplicates2(head: ListNode) -> ListNode:
        dummy_head = ListNode(None)
        dummy_head.next = head

        pre = dummy_head
        cur = head

        while cur:
            if pre and cur.val == pre.val:
                pre.next = cur.next
                cur.next = None
                cur = pre.next
                continue

            pre = cur
            cur = cur.next
        return dummy_head.next

作者：PoisonHair
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/solution/pythonfei-di-gui-he-di-gui-jie-fa-by-poisonhair/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
