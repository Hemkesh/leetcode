# https://leetcode.com/problems/generate-parentheses/
# Best submission time: 33ms

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        final = set()
        stack = [('(', 1, 0)]
        while len(stack) > 0:
            string, op, cl = stack.pop()
            if op < n:
                stack.append((string + "(", op + 1, cl))
            if cl < op:
                if op == n and cl == n-1:
                    final.add(string + ')')
                else:
                    stack.append((string + ')', op, cl + 1))
        return final