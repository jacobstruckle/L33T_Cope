from typing import List
import unittest

class Solution:
    def merge_sorted_arrays(self, array1: List[int], length1: int, array2: List[int], length2: int) -> None:
        if len(array1) < length1 + length2:
            raise ValueError("array1 does not have enough space to accommodate array2")

        index1 = length1 - 1
        index2 = length2 - 1
        merge_index = length1 + length2 - 1

        while index2 >= 0:
            if index1 >= 0 and array1[index1] > array2[index2]:
                array1[merge_index] = array1[index1]
                index1 -= 1
            else:
                array1[merge_index] = array2[index2]
                index2 -= 1
            merge_index -= 1

# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_case_1(self):
        array1 = [1, 2, 3, 0, 0, 0]
        length1 = 3
        array2 = [2, 5, 6]
        length2 = 3
        self.solution.merge_sorted_arrays(array1, length1, array2, length2)
        self.assertEqual(array1, [1, 2, 2, 3, 5, 6])

    def test_merge_case_2(self):
        array1 = [4, 5, 6, 0, 0, 0]
        length1 = 3
        array2 = [1, 2, 3]
        length2 = 3
        self.solution.merge_sorted_arrays(array1, length1, array2, length2)
        self.assertEqual(array1, [1, 2, 3, 4, 5, 6])

    def test_merge_case_3(self):
        array1 = [1, 2, 3, 0, 0, 0]
        length1 = 3
        array2 = []
        length2 = 0
        self.solution.merge_sorted_arrays(array1, length1, array2, length2)
        self.assertEqual(array1, [1, 2, 3])

    def test_merge_case_4(self):
        array1 = [0, 0, 0, 0, 0]
        length1 = 0
        array2 = [1, 2, 3, 4, 5]
        length2 = 5
        self.solution.merge_sorted_arrays(array1, length1, array2, length2)
        self.assertEqual(array1, [1, 2, 3, 4, 5])

    def test_error_for_insufficient_space(self):
        array1 = [1, 2, 3]
        length1 = 3
        array2 = [4, 5]
        length2 = 2
        with self.assertRaises(ValueError):
            self.solution.merge_sorted_arrays(array1, length1, array2, length2)

if __name__ == "__main__":
    unittest.main()
