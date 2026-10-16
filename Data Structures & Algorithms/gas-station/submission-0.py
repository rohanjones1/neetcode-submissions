class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)<sum(cost):
            return -1
        tot = 0
        curr = 0
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]
            tot += g
            tot -= c
            if tot < 0:
                curr = i+1
                tot = 0

        return curr

