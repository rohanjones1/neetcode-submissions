class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l, r = 0, n*m-1
        while l<=r:
            mid = (l+r)//m
            rem = (l+r)%m
            if matrix[mid][rem] == target:
                return True
            elif matrix[mid][rem] < target:
                l = mid*m + rem + 1
            else:
                r = mid*m + rem - 1
                
        return False
