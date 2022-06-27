# https://leetcode.com/problems/palindrome-linked-list/
# Best submission time: 76ms

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        num = []
        if head == None:
            return True
        
        while True:
            num.append(head.val)
            if head.next != None:
                head = head.next
            else:
                break
        
        i = 0
        while i < len(num)/2:
            if num[i] != num[len(num)-i-1]:
                return False
            i += 1
        return True