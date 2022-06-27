# https://leetcode.com/problems/find-all-duplicates-in-an-array/
# Best submission time: 350ms

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        sets = set()
        res = []
        for i in nums:
            if i not in sets:
                sets.add(i)
            else:
                res.append(i)
        return res