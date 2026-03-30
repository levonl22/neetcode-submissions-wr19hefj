class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        
        maxP = 0
        for p in prices:
            if p < minBuy:
                minBuy = p
            else:
                maxP = max(maxP, p - minBuy)
        return maxP