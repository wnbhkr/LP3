def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row):
    if row == len(board):
        return True

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve_n_queens(board, row + 1):
                return True

            board[row][col] = 0  # Backtrack if no solution is found

    return False

def print_board(board):
    for row in board:
        print(' '.join(['Q' if x == 1 else '.' for x in row]))

# Initialize the chessboard (8x8 in this case)
n = 8
board = [[0] * n for _ in range(n)]

# Place the first queen in a specific row and column
first_queen_row = 0
first_queen_col = 2
board[first_queen_row][first_queen_col] = 1

# Solve the N-Queens problem for the remaining queens
if solve_n_queens(board, first_queen_row + 1):
    print("Solution found:")
    print_board(board)
else:
    print("No solution found.")
