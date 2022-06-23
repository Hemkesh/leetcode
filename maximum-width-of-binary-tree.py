# https://leetcode.com/problems/maximum-width-of-binary-tree/
# Best submission time: 40ms

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = []
        q.append((root, 0, 0))
        last = 0
        max_score = 0
        cur_score = 0
        fir_score = 0
        while len(q) != 0:
            v = q.pop(0)
            node = v[0]
            index = v[1]
            level = v[2]
            if node:                   
                if last == level:
                    cur_score = index
                else:
                    cur_score = cur_score - fir_score
                    if max_score < cur_score:
                        max_score = cur_score
                    fir_score = index
            
                last = level
                q.append((node.left, index*2, level+1))
                q.append((node.right, index*2 + 1, level+1))
        
        cur_score = cur_score - fir_score
        if max_score < cur_score:
            max_score = cur_score
        return max_score + 1
