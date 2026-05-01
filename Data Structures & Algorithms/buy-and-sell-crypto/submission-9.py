class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0

        buy = 0
        sell = 1

        profit = 0
        max_profit = 0

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                profit = prices[sell] - prices[buy]
                max_profit = max(max_profit, profit)
                sell += 1
                
        return max_profit
            
        
