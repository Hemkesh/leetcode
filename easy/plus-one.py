# https://leetcode.com/problems/plus-one/
# Best submission time: 32ms

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = -1
        res = []
        for i in range(len(digits)):
            idx = len(digits) - i - 1
            if carry == -1 or carry == 1:
                digits[idx] = (digits[idx] + 1) % 10
                carry = 1 if digits[idx] == 0 else 0
            res.append(digits[idx])
        if carry == 1:
            res.append(1)
        res.reverse()
        return res
