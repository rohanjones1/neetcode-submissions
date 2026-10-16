class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for x, y in points:
            heapq.heappush(maxHeap, (-(x**2 + y**2), (x, y)))
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        ans = [y for x, y in maxHeap]
        return ans


        