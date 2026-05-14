class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxBuy = prices[0]
        maxP = 0

        for p in prices:
            if p < maxBuy:
                maxBuy = p
            maxP = max(maxP, p - maxBuy)
        return maxP