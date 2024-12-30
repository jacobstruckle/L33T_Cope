from typing import List
import unittest

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]
        return max_profit

# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        prices = [7, 1, 5, 3, 6, 4]
        self.assertEqual(self.solution.maxProfit(prices), 7)

    def test_case_2(self):
        prices = [1, 2, 3, 4, 5]
        self.assertEqual(self.solution.maxProfit(prices), 4)

    def test_case_3(self):
        prices = [7, 6, 4, 3, 1]
        self.assertEqual(self.solution.maxProfit(prices), 0)

if __name__ == "__main__":
    unittest.main()