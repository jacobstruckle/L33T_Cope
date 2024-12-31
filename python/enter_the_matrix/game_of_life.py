class Solution:
    def gameOfLife(self, board):
        # Dimensions of the board
        rows, cols = len(board), len(board[0])

        def count_live_neighbors(row, col):
            directions = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),         (0, 1),
                (1, -1), (1, 0), (1, 1)
            ]
            live_neighbors = 0

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                    live_neighbors += 1

            return live_neighbors

        # Update the board in place using marker values:
        # 2: cell was dead, becomes alive
        # -1: cell was alive, becomes dead
        for row in range(rows):
            for col in range(cols):
                live_neighbors = count_live_neighbors(row, col)

                if board[row][col] == 1:  # Live cell
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[row][col] = -1  # Mark as dead
                else:  # Dead cell
                    if live_neighbors == 3:
                        board[row][col] = 2  # Mark as alive

        # Finalize the board by converting markers to final states
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == -1:
                    board[row][col] = 0  # Dead
                elif board[row][col] == 2:
                    board[row][col] = 1  # Alive