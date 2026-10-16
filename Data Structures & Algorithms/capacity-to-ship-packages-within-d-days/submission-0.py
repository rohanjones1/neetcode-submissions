class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        while (l < r):
            mid = (l+r)//2
            counter = 1
            sumW = 0
            n = len(weights)
            for i in range(n):
                if (sumW + weights[i] > mid):
                    counter += 1
                    sumW = 0
                sumW += weights[i]
            if (counter <= days):
                r = mid
            else:
                l = mid+1
        return l
                
            



                







