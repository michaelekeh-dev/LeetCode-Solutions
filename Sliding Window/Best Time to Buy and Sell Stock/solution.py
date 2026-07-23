class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        profit = 0


        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            if profit < (prices[i] - cheapest):
                profit = prices[i] - cheapest

        return profit







        
        
