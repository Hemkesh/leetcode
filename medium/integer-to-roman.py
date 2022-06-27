# https://leetcode.com/problems/integer-to-roman/
# Best submission time: 76ms

class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M"}
        cus = 0
        ans = ""
        while cus != num:
            for n in sorted(roman.keys(), reverse=True):
                if (num - cus) % n != (num - cus):
                    cus += n
                    ans += roman[n]
                    break
        return ans