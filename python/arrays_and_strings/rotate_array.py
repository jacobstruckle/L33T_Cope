from typing import List
import unittest

class Solution:
    def rotate_array(self, nums: List[int], steps: int) -> None:

        if not nums:
            raise ValueError("Input array cannot be empty")
        
        n = len(nums)
        steps %= n
        nums[:] = nums[-steps:] + nums[:-steps]


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        steps = 3
        expected_nums = [5, 6, 7, 1, 2, 3, 4]
        self.solution.rotate_array(nums, steps)
        self.assertEqual(nums, expected_nums)

    def test_case_2(self):
        nums = [-1, -100, 3, 99]
        steps = 2
        expected_nums = [3, 99, -1, -100]
        self.solution.rotate_array(nums, steps)
        self.assertEqual(nums, expected_nums)

    def test_case_3(self):
        nums = [1]
        steps = 10
        expected_nums = [1]
        self.solution.rotate_array(nums, steps)
        self.assertEqual(nums, expected_nums)

    def test_case_4(self):
        nums = [1, 2, 3]
        steps = 0
        expected_nums = [1, 2, 3]
        self.solution.rotate_array(nums, steps)
        self.assertEqual(nums, expected_nums)

    def test_case_5(self):
        nums = [1, 2, 3, 4, 5]
        steps = 5
        expected_nums = [1, 2, 3, 4, 5]
        self.solution.rotate_array(nums, steps)
        self.assertEqual(nums, expected_nums)

    def test_empty_array(self):
        nums = []
        steps = 3
        with self.assertRaises(ValueError):
            self.solution.rotate_array(nums, steps)

if __name__ == "__main__":
    unittest.main()
