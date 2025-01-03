class Solution:
    def spiralOrder(self, matrix):
        spiral_sequence = []

        if not matrix or not matrix[0]:
            return spiral_sequence

        top_row, bottom_row = 0, len(matrix) - 1
        left_column, right_column = 0, len(matrix[0]) - 1

        while top_row <= bottom_row and left_column <= right_column:
            for col in range(left_column, right_column + 1):
                spiral_sequence.append(matrix[top_row][col])
            top_row += 1

            for row in range(top_row, bottom_row + 1):
                spiral_sequence.append(matrix[row][right_column])
            right_column -= 1

            if top_row <= bottom_row:
                for col in range(right_column, left_column - 1, -1):
                    spiral_sequence.append(matrix[bottom_row][col])
                bottom_row -= 1

            if left_column <= right_column:
                for row in range(bottom_row, top_row - 1, -1):
                    spiral_sequence.append(matrix[row][left_column])
                left_column += 1

        return spiral_sequence