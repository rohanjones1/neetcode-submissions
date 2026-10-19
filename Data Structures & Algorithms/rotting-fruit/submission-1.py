from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = dr+r, dc+c
                    if row in range(0, len(grid)) and col in range(0, len(grid[0])) and grid[row][col] == 1:
                        q.append((row, col))
                        grid[row][col] = 2
                        fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1
