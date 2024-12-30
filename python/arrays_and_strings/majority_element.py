from typing import List
import unittest

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("Input list cannot be empty")

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [3, 2, 3]
        self.assertEqual(self.solution.majorityElement(nums), 3)

    def test_case_2(self):
        nums = [2, 2, 1, 1, 1, 2, 2]
        self.assertEqual(self.solution.majorityElement(nums), 2)

    def test_case_3(self):
        nums = [1]
        self.assertEqual(self.solution.majorityElement(nums), 1)

    def test_case_4(self):
        nums = [1, 1, 2, 2, 2, 2, 2]
        self.assertEqual(self.solution.majorityElement(nums), 2)

    def test_case_5(self):
        nums = [4, 4, 4, 4]
        self.assertEqual(self.solution.majorityElement(nums), 4)

    def test_empty_list(self):
        nums = []
        with self.assertRaises(ValueError):
            self.solution.majorityElement(nums)

if __name__ == "__main__":
    unittest.main()
