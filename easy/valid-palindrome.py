# https://leetcode.com/problems/valid-palindrome/
# Best submission time: 44ms

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        lt = [x.lower() for x in s if x.isalnum()]
        return lt == lt[::-1]