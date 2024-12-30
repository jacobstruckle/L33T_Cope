from typing import List
import unittest

class Solution:
    def remove_duplicates(self, nums: List[int]) -> int:
        if not nums:
            raise ValueError("Input list cannot be empty")

        write_position = 0

        for num in nums:
            if write_position < 2 or nums[write_position - 2] != num:
                nums[write_position] = num
                write_position += 1

        return write_position

# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [1, 1, 1, 2, 2, 3]
        expected_nums = [1, 1, 2, 2, 3]
        new_length = self.solution.remove_duplicates(nums)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(nums[:new_length], expected_nums)

    def test_case_2(self):
        nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
        expected_nums = [0, 0, 1, 1, 2, 3, 3]
        new_length = self.solution.remove_duplicates(nums)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(nums[:new_length], expected_nums)

    def test_case_3(self):
        nums = [1, 1, 2]
        expected_nums = [1, 1, 2]
        new_length = self.solution.remove_duplicates(nums)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(nums[:new_length], expected_nums)

    def test_case_4(self):
        nums = []
        with self.assertRaises(ValueError):
            self.solution.remove_duplicates(nums)

    def test_case_5(self):
        nums = [1, 1, 1, 1]
        expected_nums = [1, 1]
        new_length = self.solution.remove_duplicates(nums)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(nums[:new_length], expected_nums)

    def test_case_6(self):
        nums = [1, 2, 2, 3, 3, 3]
        expected_nums = [1, 2, 2, 3, 3]
        new_length = self.solution.remove_duplicates(nums)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(nums[:new_length], expected_nums)

if __name__ == "__main__":
    unittest.main()