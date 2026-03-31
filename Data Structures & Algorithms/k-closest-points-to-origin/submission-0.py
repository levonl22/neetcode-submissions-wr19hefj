class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        distances = []
        for p in points:
            dist = (p[0] ** 2 + p[1] ** 2)
            distances.append([dist, p[0], p[1]])
        
        heapq.heapify(distances)
        res = []
        while len(res) < k:
            p, x, y = heapq.heappop(distances)
            res.append([x, y])
        
        return res
        
