class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()

        max = 0
        length = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                i = i + 1
            elif nums[i+1] - nums[i] == 1:
                length = length + 1
                if length > max:
                    max = length
            else:
                length = 0
        return max + 1