class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if (n==0):
            return 0

        prefix = [0]*n
        suffix = [0]*n

        maxL = 0
        for i in range(len(height)):
            prefix[i] = maxL
            maxL = max(maxL, height[i])

        maxR = 0
        for i in range(len(height)-1, -1, -1):
            suffix[i] = maxR
            maxR = max(maxR, height[i])
        area = 0
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            if water>0:
                area += water
        return area
    