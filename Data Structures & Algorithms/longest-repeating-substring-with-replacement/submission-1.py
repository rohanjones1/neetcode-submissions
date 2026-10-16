class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        chars = {}
        n = len(s)
        maxLen = 0
        while (r < n):
            char = s[r]
            if (char in chars):
                chars[char] += 1
            else:
                chars[char] = 1
            
            while (r-l+1) - max(chars.values()) > k:
                chars[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r-l+1)
            r += 1

        return maxLen

            


