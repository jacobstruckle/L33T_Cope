from typing import List
import unittest

class Solution:
    def remove_element(self, nums: List[int], value_to_remove: int) -> int:
        new_length = 0
        for i in range(len(nums)):
            if nums[i] != value_to_remove:
                nums[new_length] = nums[i]
                new_length += 1
        return new_length

# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [3, 2, 2, 3]
        value_to_remove = 3
        expected_nums = [2, 2]
        new_length = self.solution.remove_element(nums, value_to_remove)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(sorted(nums[:new_length]), sorted(expected_nums))

    def test_case_2(self):
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        value_to_remove = 2
        expected_nums = [0, 1, 3, 0, 4]
        new_length = self.solution.remove_element(nums, value_to_remove)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(sorted(nums[:new_length]), sorted(expected_nums))

    def test_case_3(self):
        nums = [1, 1, 1, 1]
        value_to_remove = 1
        expected_nums = []
        new_length = self.solution.remove_element(nums, value_to_remove)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(nums[:new_length], expected_nums)

    def test_case_4(self):
        nums = [1, 2, 3, 4, 5]
        value_to_remove = 6
        expected_nums = [1, 2, 3, 4, 5]
        new_length = self.solution.remove_element(nums, value_to_remove)
        self.assertEqual(new_length, len(expected_nums))
        self.assertEqual(nums[:new_length], expected_nums)

if __name__ == "__main__":
    unittest.main()
