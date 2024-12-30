class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_win = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > max_win:
                    max_win = profit
        return max_win
solution = Solution()
prices1 = [7, 1, 5, 3, 6, 4]
prices2 = [7, 6, 4, 3, 1]
print(solution.maxProfit(prices1))
print(solution.maxProfit(prices2))