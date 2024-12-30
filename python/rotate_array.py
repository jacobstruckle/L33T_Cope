class Solution:
    def rotate_array(self, array, steps):
        length = len(array)
        steps = steps % length
        array[:] = array[-steps:] + array[:-steps]
solution = Solution()
nums1 = [1, 2, 3, 4, 5, 6, 7]
steps1 = 3
solution.rotate_array(nums1, steps1)
print(nums1)
nums2 = [-1, -100, 3, 99]
steps2 = 2
solution.rotate_array(nums2, steps2)
print(nums2)