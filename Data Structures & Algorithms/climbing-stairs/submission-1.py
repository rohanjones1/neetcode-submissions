class Solution:
    def climbStairs(self, n: int) -> int:
        # if (n == 1 or n == 0):
        #     return 1
        # return self.climbStairs(n-1) + self.climbStairs(n-2)

        one, two = 1, 1
        for i in range(n-1):
            temp = one
            one = one+two
            two = temp
        return one
