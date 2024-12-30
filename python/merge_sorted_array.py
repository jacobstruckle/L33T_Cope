class Solution:
    def merge_sorted_arrays(self, array1, length1, array2, length2):
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

solution = Solution()

array1 = [1, 2, 3, 0, 0, 0]
length1 = 3
array2 = [2, 5, 6]
length2 = 3

solution.merge_sorted_arrays(array1, length1, array2, length2)
print(array1)
