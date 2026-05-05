class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left, right = 0, len(matrix[0]) - 1
        top, bot = 0, len(matrix) - 1

        while left <= right and top <= bot:
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            for row in range(top, bot + 1):
                res.append(matrix[row][right])
            right -= 1

            if not (left <= right and top <= bot):
                break
            
            for col in range(right, left - 1, -1):
                res.append(matrix[bot][col])
            bot -= 1

            for row in range(bot, top - 1, -1):
                res.append(matrix[row][left])
            left += 1
        
        return res