class Solution:
    def isValidSudoku(self, board):
        def is_valid_group(elements):
            filtered_elements = [e for e in elements if e != '.']
            return len(filtered_elements) == len(set(filtered_elements))

        for row in board:
            if not is_valid_group(row):
                return False

        for col_index in range(9):
            column = [board[row_index][col_index] for row_index in range(9)]
            if not is_valid_group(column):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                sub_box = [
                    board[row][col]
                    for row in range(box_row, box_row + 3)
                    for col in range(box_col, box_col + 3)
                ]
                if not is_valid_group(sub_box):
                    return False

        return True