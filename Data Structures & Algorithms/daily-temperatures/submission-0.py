class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        t = len(temperatures)
        res = [0]*t
        for i in range(1, t):
            while (stack and temperatures[i]>temperatures[stack[-1]]):
                res[stack[-1]] = i-stack[-1]
                stack.pop()
            stack.append(i)
                
        return res
        



            
