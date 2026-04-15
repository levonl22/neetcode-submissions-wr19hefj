class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxProfit = 0

        for p in prices:
            if p < minBuy:
                minBuy = p
            if p - minBuy > maxProfit:
                maxProfit = p - minBuy
        return maxProfit