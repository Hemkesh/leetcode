# https://leetcode.com/problems/valid-parentheses/
# Best submission time: 26ms

class Solution:
    def isValid(self, s: str) -> bool:
        op = {'(' : 0, '[' : 1, '{' : 2}
        cl = {')' : 0, ']' : 1, '}' : 2}
        stack = []
        for i in s:
            if i in op:
                stack.append(i)
            elif i in cl and len(stack) > 0:
                if cl[i] == op[stack[-1]]:
                    stack.pop()
                else: return False
            else: return False
        return not len(stack)