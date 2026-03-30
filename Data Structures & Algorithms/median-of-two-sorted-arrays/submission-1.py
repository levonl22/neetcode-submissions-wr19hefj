class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list = nums1 + nums2
        list = sorted(list)

        l, r = 0, len(list) - 1
        if len(list) % 2 == 0:
            l = r // 2
            r = l + 1
            m = (list[l] + list[r]) / 2
            return m
        else:
            m = r // 2
            return list[m]
            