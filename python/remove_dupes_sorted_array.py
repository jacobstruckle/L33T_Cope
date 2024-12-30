class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        unique_index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[unique_index]:
                unique_index += 1
                nums[unique_index] = nums[i]
        return unique_index + 1

if __name__ == "__main__":
    solution = Solution()
    nums1 = [1, 1, 2]
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    k1 = solution.removeDuplicates(nums1)
    print("Output:", k1, ", nums =", nums1[:k1])
    k2 = solution.removeDuplicates(nums2)
    print("Output:", k2, ", nums =", nums2[:k2])