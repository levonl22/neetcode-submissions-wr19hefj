class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = collections.deque()
        time, fresh = 0, 0

        def rot(r, c):
            if (r < 0 or r == ROWS or c < 0 or c == COLS or
                grid[r][c] == 2 or grid[r][c] == 0 or (r, c) in visit):
                return
            visit.add((r, c))
            q.append((r, c))
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row < 0 or row == ROWS or
                        col < 0 or col == COLS or
                        grid[row][col] != 1):
                        continue
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1
            time += 1

        return time if fresh == 0 else -1