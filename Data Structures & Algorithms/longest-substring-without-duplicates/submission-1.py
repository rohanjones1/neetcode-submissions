class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # string = set()
        # n = len(s)
        # if (n == 0):
        #     return 0
        # p1, p2 = 0, 0
        # ans = 0
        # sub = 0
        # while (p1 < n and p2 < n):
        #     if s[p2] in string:
        #         ans = max(ans, sub)
        #         sub = 0
        #         string = set()
        #         p1 += 1
        #         p2 = p1
        #     else:
        #         string.add(s[p2])
        #         p2 += 1
        #         sub += 1
        # return ans










        subString = set()
        maxLen = 0
        subLen = 0
        l, r = 0, 0
        n = len(s)
        while (r < n):
            while s[r] in subString:
                subString.remove(s[l])
                subLen -= 1
                l += 1
            subString.add(s[r])
            maxLen = max(maxLen, r-l+1)
            r += 1
        return maxLen



            
            


