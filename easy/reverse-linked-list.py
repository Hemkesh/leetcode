# https://leetcode.com/problems/reverse-linked-list
# Best submission time: 39ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prev, curr = head, head.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev, curr = curr, nxt
        head.next = None
        return prev