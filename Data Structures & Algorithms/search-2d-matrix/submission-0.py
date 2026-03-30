class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l, r = 0, len(row) - 1
            if row[r] < target:
                continue
            else:
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] < target:
                        l += 1
                    elif row[mid] > target:
                        r -= 1
                    else:
                        return True
        return False