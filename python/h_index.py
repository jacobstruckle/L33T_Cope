from typing import List
import unittest

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations, reverse=True)
        h_index = 0

        for i, citation_count in enumerate(sorted_citations):
            if citation_count >= i + 1:
                h_index = i + 1
            else:
                break

        return h_index

# Unit tests
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        citations = [3, 0, 6, 1, 5]
        self.assertEqual(self.solution.hIndex(citations), 3)

    def test_case_2(self):
        citations = [1, 3, 1]
        self.assertEqual(self.solution.hIndex(citations), 1)

    def test_case_3(self):
        citations = [0, 0, 0, 0]
        self.assertEqual(self.solution.hIndex(citations), 0)

    def test_case_4(self):
        citations = [10, 8, 5, 4, 3]
        self.assertEqual(self.solution.hIndex(citations), 4)

    def test_case_5(self):
        citations = []
        self.assertEqual(self.solution.hIndex(citations), 0)

if __name__ == "__main__":
    unittest.main()
