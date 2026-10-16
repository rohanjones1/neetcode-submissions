class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder = sorted(folder)
        ans = [folder[0]]

        for i in range(1, len(folder)):
            parentPrefix = ans[-1] + "/"
            if parentPrefix not in folder[i]:
                ans.append(folder[i])
        return ans

