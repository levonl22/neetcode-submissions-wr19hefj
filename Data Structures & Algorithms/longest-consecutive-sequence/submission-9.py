class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0

        for n in nums:
            curr = 1
            if n - 1 not in seen:
                while n + curr in seen:
                    curr += 1
                longest = max(longest, curr)
        return longest