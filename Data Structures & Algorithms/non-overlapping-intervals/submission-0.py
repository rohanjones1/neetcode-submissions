class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        if len(intervals) == 1:
            return 0

        intervals = sorted(intervals)
        ans = 0
        end = intervals[0][1]
        for i in range(1, n):
            if (end > intervals[i][0]):
                end = min(end, intervals[i][1])
                ans += 1
            else:
                end = intervals[i][1]
        return ans