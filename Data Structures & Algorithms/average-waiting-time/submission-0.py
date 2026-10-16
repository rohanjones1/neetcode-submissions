class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        n = len(customers)
        ptr = customers[0][0]
        for arrival, time in customers:
            waiting = arrival-ptr
            if waiting<0:
                waiting = -waiting
            else:
                waiting = 0
                ptr = arrival
            ptr += time
            waiting += time
            total += waiting
        return total/n
            
            