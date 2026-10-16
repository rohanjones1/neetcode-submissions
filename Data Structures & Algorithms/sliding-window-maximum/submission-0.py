from collections import deque
import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        for i in range(k-1):
            heap.append((-nums[i], -i))
        heapq.heapify(heap)
        ans = []
        for r in range(k-1, len(nums)):
            heapq.heappush(heap, (-nums[r], -r))
            while True:
                top = heap[0]
                if -top[1]>r-k:
                    break
                else:
                    heapq.heappop(heap)
            ans.append(-top[0])
        return ans



            



