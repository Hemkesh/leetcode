# https://leetcode.com/problems/maximum-width-of-binary-tree
# Best submission time: 40ms

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = lef
        self.right = right

# Logic: Use Level-Order Traversal
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        
        q = [root]
        res = 0
        root.val = 0
        
        while len(q) != 0:
            n = len(q)
            while n > 0:
                node = q.pop(0)
                n -= 1
                if node.left:
                    node.left.val = 2 * node.val
                    q.append(node.left)
                if node.right:
                    node.right.val = 2 * node.val + 1
                    q.append(node.right)
            
            if len(q) > 1: res = max(q[-1].val - q[0].val, res)
                
        return res + 1