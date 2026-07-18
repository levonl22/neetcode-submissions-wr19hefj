class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        min_buy = prices[0]

        l = 0
        for r in range(len(prices)):
            profit = prices[r] - min_buy
            if prices[r] < prices[l]:
                l = r
                min_buy = prices[l]
            else:
                res = max(res, profit)

        return res         