class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minBuy = prices[0]
        maxP = 0

        for price in prices:
            if price < minBuy:
                minBuy = price
            maxP = max(maxP, price - minBuy)
        
        return maxP