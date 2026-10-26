class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            j, k = i+1, len(nums)-1

            if i>0 and nums[i-1] == nums[i]:
                continue

            curr = nums[i]
            while (j<k):
                check = nums[j]+nums[k]
                if check == -curr:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                elif check > -curr:
                    k -= 1
                    
                elif check < -curr:
                    j += 1
                    
        
        return ans


