# https://leetcode.com/problems/first-unique-character-in-a-string/
# Best submission time: 93ms
 
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        once = set()
        for idx, ch in enumerate(s):
            if ch not in dic:
                dic[ch] = idx
                once.add(ch)
            elif ch in once:
                once.remove(ch)
        return -1 if not len(once) else min([dic[x] for x in once])