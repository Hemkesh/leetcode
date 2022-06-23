# https://leetcode.com/problems/reverse-integer
# Best submission time: 36ms

class Solution:
    def reverse(self, x: int) -> int:
        neg = False 
        if x < 0:
            neg = True
            x *= -1
        res = 0
        while x > 0:
            res = res * 10 + x%10
            x = x//10
        if res > 2**31:
            return 0
        if neg:
            return -res 
        return res 