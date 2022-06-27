# https://leetcode.com/problems/palindrome-number/
# Best submission time: 90ms

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif x >= 0 and x <= 9:
            return True
        y, og = x, x
        size = -1
        while x != 0:
            x = x // 10
            size += 1
        n = 0
        while y != 0:
            n += ((y % 10) * 10**size)
            y = y // 10
            size -= 1
        return og == n