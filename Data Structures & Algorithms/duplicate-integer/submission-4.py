class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        nums.sort()
        pre = nums[0]
        for i in range (1, len(nums)):
            if nums[i] == pre:
                return True
            pre = nums[i]
        return False