class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            comp = target - n
            if comp in seen:
                return [seen[comp] + 1, i + 1]
            seen[n] = i
        return []