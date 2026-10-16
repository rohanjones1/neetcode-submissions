class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [float('inf')] * len(nums)
        memo[0] = 0
        for i in range(len(nums)-1):
            for j in range(1, nums[i]+1):
                if (i+j<len(nums)):
                    memo[i+j] = min(memo[i]+1, memo[i+j])
        return memo[-1]

