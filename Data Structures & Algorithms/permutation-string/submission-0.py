class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l, r = 0, len(s1) - 1
        counts1 = {}
        counts2 = {}

        for i in range(r + 1):
            counts1[s1[i]] = counts1.get(s1[i], 0) + 1
            counts2[s2[i]] = counts2.get(s2[i], 0) + 1

        if counts1 == counts2:
            return True

        r += 1

        while r < len(s2):
            counts2[s2[r]] = counts2.get(s2[r], 0) + 1

            counts2[s2[l]] -= 1
            if counts2[s2[l]] == 0:
                del counts2[s2[l]]

            l += 1

            if counts1 == counts2:
                return True

            r += 1

        return False