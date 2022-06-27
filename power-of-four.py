# https://leetcode.com/problems/power-of-four/
# Best submission time: 28ms

import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        elif num % 4 != 0 or num < 4:
            return False
        else:
            return (math.log(num)/math.log(4)) % 1 == 0