# Sudoku Solver in Python
def is_valid(board, row, col, num):
    # Check the row
    for x in range(8):
        if board[row][x] == num:
            return False

    # Check the column
    for x in range(8):
        if board[x][col] == num:
            return False

    # Check the box
    start_row = row - row % 2
    start_col = col - col % 4
    for i in range(2):
        for j in range(4):
            if board[i + start_row][j + start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                for num in range(1, 9):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

def print_board(board):
    for i in range(8):
        if i % 2 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(8):
            if j % 4 == 0 and j != 0:
                print(" | ", end="")

            if j == 7:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def main():
    board = [
        [5, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    if solve_sudoku(board):
        print_board(board)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()