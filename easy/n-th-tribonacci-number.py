# https://leetcode.com/problems/n-th-tribonacci-number/submissions/
# Best submission time: 16ms

dic = {0: 0, 1: 1, 2: 1}

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in dic:
            return dic[n]
        res = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        dic[n] = res
        return res