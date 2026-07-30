class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        minL = [0]* len(prices)
        # minval = 1000
        # for i in range(len(prices)):
        #     minL[i] = min(minval,prices[i])
        #     if(prices[i]<minval):
        #         minval = prices[i]
        max_profit = 0
        minval = prices[0]
        for i in range(1,len(prices)):
            minL[i] = min(minval,prices[i])
            if(prices[i]<minval):
                minval = prices[i]
            profit = prices[i]-minL[i]
            if profit <=0:
                continue
            else:
                if(profit>max_profit):
                    max_profit = profit  



        return max_profit
        