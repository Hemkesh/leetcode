# https://leetcode.com/problems/roman-to-integer/
# Best submission time: 54ms

class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        res, i = 0, 0
        while i != len(s):
            if s[i] in {'I', 'X', 'C'} and i != len(s) - 1 and s[i] + s[i+1] in romans:
                res += romans[s[i] + s[i+1]]
                i += 1
            else:
                res += romans[s[i]]
            i += 1
        return res