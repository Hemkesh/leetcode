# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Best submission time: 440ms

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        for index, i in enumerate(s):
            sub = {i: True}
            if index != len(s)-1:
                for j in s[index+1:]:
                    if j not in sub:
                        sub[j] = True
                    else:
                        break
                if len(sub) > m:
                    m = len(sub)
            else:
                if len(sub) > m:
                    m = len(sub)
                break
        return m