# https://leetcode.com/problems/add-two-numbers/
# Best submission time: 76ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = ListNode()
        head = out
        c = 0
        while l1 or l2:
            if l1 and l2:
                out.val = (l1.val + l2.val + c) % 10
                c = 1 if l1.val + l2.val + c > 9 else 0
            else:
                out.val = ((l1.val if l1 else l2.val) + c) % 10
                c = 1 if ((l1.val if l1 else l2.val) + c) > 9 else 0
                if c == 0:
                    out.next = l1.next if l1 else l2.next
                    break
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            if l1 or l2 or c:
                out.next = ListNode()
                out = out.next
        if c: out.val = 1
        return head