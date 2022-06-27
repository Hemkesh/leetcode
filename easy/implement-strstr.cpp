// https://leetcode.com/problems/implement-strstr/
// Best submission time: 14ms

class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle == ""){
            return 0;
        }
        auto ans = haystack.find(needle);
        if (ans == string::npos){
            return -1;
        }
        return ans;
    }
};