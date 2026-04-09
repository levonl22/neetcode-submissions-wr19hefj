class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)

        longest = 0
        for n in nums:
            streak = 1
            if n - 1 not in numSet:
                while n + streak in numSet:
                    streak += 1
                longest = max(longest, streak)
        return longest