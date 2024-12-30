class Solution:
    @staticmethod
    def remove_element(nums, value_to_remove):
        new_length = 0
        for i in range(len(nums)):
            if nums[i] != value_to_remove:
                nums[new_length] = nums[i]
                new_length += 1
        return new_length

def test_remove_element():
    solution = Solution()

    input_array_1 = [3, 2, 2, 3]
    value_to_remove_1 = 3
    expected_output_1 = [2, 2]
    result_length_1 = solution.remove_element(input_array_1, value_to_remove_1)
    assert result_length_1 == len(expected_output_1), f"Expected length {len(expected_output_1)}, but got {result_length_1}"
    assert sorted(input_array_1[:result_length_1]) == sorted(expected_output_1), f"Expected {expected_output_1}, but got {input_array_1[:result_length_1]}"

    input_array_2 = [0, 1, 2, 2, 3, 0, 4, 2]
    value_to_remove_2 = 2
    expected_output_2 = [0, 1, 3, 0, 4]
    result_length_2 = solution.remove_element(input_array_2, value_to_remove_2)
    assert result_length_2 == len(expected_output_2), f"Expected length {len(expected_output_2)}, but got {result_length_2}"
    assert sorted(input_array_2[:result_length_2]) == sorted(expected_output_2), f"Expected {expected_output_2}, but got {input_array_2[:result_length_2]}"

    print("All test cases passed.")

test_remove_element()
