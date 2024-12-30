class Solution:
    def remove_duplicates(self, numbers):
        write_position = 0
        for number in numbers:
            if write_position < 2 or numbers[write_position - 2] != number:
                numbers[write_position] = number
                write_position += 1
        return write_position
solution = Solution()
nums1 = [1, 1, 1, 2, 2, 3]
result1 = solution.remove_duplicates(nums1)
print(result1, nums1[:result1])
nums2 = [0, 0, 1, 1, 1, 1, 2, 3, 3]
result2 = solution.remove_duplicates(nums2)
print(result2, nums2[:result2])
