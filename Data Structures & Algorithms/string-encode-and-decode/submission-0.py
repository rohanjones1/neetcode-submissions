class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for i in strs:
            ans += str(len(i)) + "#" + i
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while (i<len(s)):
            num = ""
            word = ""
            letter = s[i]
            while (letter != "#"):
                num += letter
                i += 1
                letter = s[i]
            i += 1
            intNum = int(num)
            for j in range(intNum):
                word += s[i+j]
            i += intNum
            ans.append(word)
        return ans


