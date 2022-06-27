# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/
# Best submission time: 1095ms

class Solution:
    def minCost(self, S: str, C: List[int]) -> int:
        last = S[0]
        last_score = C[0]
        total = 0
        for i in range(1,len(S)):
            if S[i] == last:
                total += min(last_score, C[i])
                last_score = max(last_score, C[i])
            else:
                last = S[i]
                last_score = C[i]
        return total