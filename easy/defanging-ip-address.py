# https://leetcode.com/problems/defanging-an-ip-address/
# Best submission time: 33ms

class Solution:
    def defangIPaddr(self, address: str) -> str:
        # one line sol
        # return "[.]".join(address.split('.'))
        
        # second one liner
        # return address.replace(".", "[.]")
        
        # not using any default functions
        res = ""
        num = ""
        for i in address:
            if i.isdigit():
                num += i
            else:
                res = res + num + "[.]"
                num = ""
        res += num
        return res