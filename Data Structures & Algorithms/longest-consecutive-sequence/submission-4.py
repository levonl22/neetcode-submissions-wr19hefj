class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        largest = 0
        for n in nums:
            if n - 1 not in numSet:
                streak = 0
                while n + streak in numSet:
                    streak += 1
                largest = max(largest, streak)
        return largest