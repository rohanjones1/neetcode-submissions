class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = {}
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 1

        required = len(t_dict)
        formed = 0

        l = 0
        ans = ""
        min_len = float("inf")

        for r in range(len(s)):
            char_r = s[r]
            if char_r in t_dict:
                t_dict[char_r] -= 1
                if t_dict[char_r] == 0:
                    formed += 1
            
            while (formed == required):
                if (r-l+1 < min_len):
                    min_len = r-l+1
                    ans = s[l:r+1]

                char_l = s[l]

                if char_l in t_dict:
                    t_dict[char_l] += 1
                    if t_dict[char_l] > 0:
                        formed -= 1
                l += 1

        return ans

        
            
            




