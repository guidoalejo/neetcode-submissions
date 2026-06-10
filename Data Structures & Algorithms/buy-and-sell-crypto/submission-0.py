class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1

        max_profit = 0

        while right < len(prices): # iterate through the list

            if prices[left] < prices[right]: # if there is actual profit

                profit = prices[right] - prices[left] 

                if profit > max_profit:

                    max_profit = profit # update the bigger profit

            else:
                left = right # if right is lower price than left, buy at that lower price

            right += 1

        return max_profit
