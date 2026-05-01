class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) <= 1:
            return 0

        day = 0 
        buy = 0
        sell = 1

        stocks = []

        while sell < len(prices):
            if prices[buy] > prices[sell]:
                buy = sell
                sell += 1
            else:
                stocks.append(prices[sell] - prices[buy])
                sell += 1

        profit = 0
        for i in range(len(stocks)):
            if stocks[i] > profit:
                profit = stocks[i]

        return profit
            
        
