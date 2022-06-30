# https://leetcode.com/problems/longest-consecutive-sequence/
# Best submission time: 630ms

class Node:
    def __init__(self, val, weight = 0, visited = False):
        self.val, self.weight, self.visited = val, weight, visited

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        map = {}
        nodes = {}
        for n in nums:
            map[n] = n+1 if n+1 in map else None
            if n-1 in map: map[n-1] = n
            nodes[n] = Node(n)

        max_wt = 0
        for k in map.keys():
            node = nodes[k]
            if not node.visited:
                i = 1
                temp = map[k]
                while temp is not None:
                    other = nodes[temp]
                    if other.visited:
                        i += other.weight
                        break
                    else:
                        other.visited = True
                    temp = map[temp]
                    i += 1
                node.visited = True
                node.weight = i
                max_wt = max(max_wt, node.weight)
        return max_wt