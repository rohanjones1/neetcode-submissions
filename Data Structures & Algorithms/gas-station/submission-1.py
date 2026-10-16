class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        surplus = 0
        tot = 0
        curr = 0
        for i in range(len(gas)):
            g = gas[i]
            c = cost[i]
            surplus += g
            surplus -= c
            tot += g
            tot -= c
            if tot < 0:
                curr = i+1
                tot = 0

        if surplus<0:
            return -1
        return curr

