# https://leetcode.com/problems/3sum/
# Best submission time: 4357 ms

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) > 2:
            if set(nums) == {0}:
                return [[0,0,0]]
            data = {}
            for idx, num in enumerate(nums):
                if num not in data: data[num] = set()
                data[num].add(idx)
            res = set()
            for i, ni in enumerate(nums):
                for k, nj in enumerate(nums[i + 1:]):
                    j = k+1+i
                    find = -1 * (ni + nj)
                    if find in data and i!=j:
                        if i not in data[find] and j not in data[find]:
                            res.add(tuple(sorted([find, ni, nj])))
                        elif i in data[find] and j not in data[find] and len(data[find]) > 1:
                            res.add(tuple(sorted([find, ni, nj])))
                        elif j in data[find] and i not in data[find] and len(data[find]) > 1:
                            res.add(tuple(sorted([find, ni, nj])))
                        elif i in data[find] and j in data[find] and len(data[find]) > 2:
                            res.add(tuple(sorted([find, ni, nj])))
            return res