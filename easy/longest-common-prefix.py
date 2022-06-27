# https://leetcode.com/problems/longest-common-prefix/submissions/
# Best submission time: 40ms

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        if len(strs)==1: 
            return strs[0]
        prefix = strs[0]
        for word in strs[1:]:
            temp = ""
            i = 0
            for ch in prefix:
                if i < len(word) and ch == word[i]:
                    temp += ch
                else:
                    break
                i += 1
            prefix = temp
        return prefix