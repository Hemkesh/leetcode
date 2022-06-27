# https://leetcode.com/problems/height-checker/
# Best submission time: 20ms

class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        original = heights[:]
        heights.sort()
        res = 0
        for i in range(len(heights)):
            res = res + 1 if heights[i] != original[i] else res
        return res