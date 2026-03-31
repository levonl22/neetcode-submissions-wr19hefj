class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        p = []
        heapq.heapify(p)

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heapq.heappush(p, [dist, x, y])
        
        res = []
        while len(res) < k:
            dist, x, y = heapq.heappop(p)
            res.append([x, y])
        
        return res