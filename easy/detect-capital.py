# https://leetcode.com/problems/detect-capital
# Best submission time: 24ms

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        lst = []
        for i, x in enumerate(word):
            if x.isupper():
                lst.append(i)
        if len(lst) == len(word):
            return True
        elif len(lst) == 0:
            return True
        elif len(lst) == 1 and lst[0] == 0:
            return True
        return False
        