# https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
# # Best submission time: 28ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        length = 0
        while node is not None:
            length += 1
            node = node.next
            
        ans = 0
        
        node = head
        while node is not None:
            ans += node.val * (2** (length-1))
            length -= 1
            node= node.next
            
        return ans