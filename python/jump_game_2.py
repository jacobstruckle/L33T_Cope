from typing import List
import unittest

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= n - 1:
                    break
        
        return jumps

# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        nums = [2, 3, 1, 1, 4]
        self.assertEqual(self.solution.jump(nums), 2)

    def test_case_2(self):
        nums = [2, 3, 0, 1, 4]
        self.assertEqual(self.solution.jump(nums), 2)

    def test_case_3(self):
        nums = [0]
        self.assertEqual(self.solution.jump(nums), 0)

    def test_case_4(self):
        nums = [1, 2, 3]
        self.assertEqual(self.solution.jump(nums), 2)

    def test_case_5(self):
        nums = [1, 1, 1, 1]
        self.assertEqual(self.solution.jump(nums), 3)

    def test_case_6(self):
        nums = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 1]
        self.assertEqual(self.solution.jump(nums), 2)

    def test_empty_array(self):
        nums = []
        self.assertEqual(self.solution.jump(nums), 0)

if __name__ == "__main__":
    unittest.main()
