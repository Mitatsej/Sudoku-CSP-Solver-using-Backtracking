#Krijimi i tabeles sudoku 9x9
board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

def is_valid(board, row, col, num):
    # Kontrollo rreshtin
    for i in range(9):
        if board[row][i] == num:
            return False
    # Kontrollo në kolonë
    for i in range(9):
        if board[i][col] == num:
            return False

    # Kontrollo në bllokun 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def solve_sudoku(board):

    for row in range(9):
        for col in range(9):
            if board[row][col] == 0: # Gjej qelizën bosh

                for num in range(1, 10): # Provo vlerat nga 1 në 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num # Vendos vlerën


                        if solve_sudoku(board): # Rekursioni
                            return True


                        board[row][col] = 0  # Backtrack

                return False # Nëse nuk ka zgjidhje
    return True   # Sudoku u zgjidh



def forward_checking(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                possible_values = [num for num in range(1, 10) if is_valid(board, row, col, num)]
                if not possible_values:  # Nëse nuk ka vlerë të vlefshme
                    return False
    return True



def print_board(board):
    for row in board:
        print(row)



if __name__ == "__main__":
    if solve_sudoku(board):
        print("Sudoku u zgjidh:")
        print_board(board)
    else:
        print("Nuk ka zgjidhje për këtë Sudoku.")
