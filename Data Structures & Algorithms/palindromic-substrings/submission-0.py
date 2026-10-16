class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def expand(x, y):
            n = 0
            while (x>=0 and y<len(s) and s[x]==s[y]):
                n += 1
                x -= 1
                y += 1
            return n


        for i in range(len(s)-1):
            ans += expand(i, i)
            ans += expand(i, i+1)

        return ans + 1

        


