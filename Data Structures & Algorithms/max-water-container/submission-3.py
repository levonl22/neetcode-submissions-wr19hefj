class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        maxA = 0
        while l < r:
            a = (r - l) * min(heights[l], heights[r])
            maxA = max(a, maxA)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxA