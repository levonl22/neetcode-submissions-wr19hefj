class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0

        for p in prices:
            if p < minBuy:
                minBuy = p
            elif p - minBuy > maxP:
                maxP = p - minBuy
        
        return maxP