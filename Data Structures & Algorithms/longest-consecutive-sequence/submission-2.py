class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = set(nums)
        nums = sorted(nums)

        high = 1
        rec = 1

        for i in range(len(nums)):
            if i < len(nums) - 1 and nums[i + 1] - nums[i] == 1:
                rec += 1
                high = max(high, rec)
            else:
                rec = 1
        return high 