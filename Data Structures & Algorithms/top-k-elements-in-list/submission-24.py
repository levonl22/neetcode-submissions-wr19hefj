class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count map with key (freq) and val (num)
        # freq buckets to keep frequencies of nums
        # reverse through freq and put into res array
        # if len res arr == k, return

        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        