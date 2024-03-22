import copy
from typing import List

board1 = [
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

board2 = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 6, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 3, 0],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]


def print_board(board: List[List[int]] | None) -> None :
    if board is None or not board:
        print("No board to display or the board is empty (Maybe it couldn't be solved).")
        return None

    board_has_9_rows = (len(board) == 9)
    all_row_are_length_9 = True
    for i in range(len(board)):
        if len(board[i]) != 9:
            all_row_are_length_9 = False
            break
        
    if not board_has_9_rows or not all_row_are_length_9:
        print("""Board isn't at the right format.
It should be 9*9 int list with 0 <= int < 10.
Please follow the following format :
    board = [
        [8, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, 6, 0, 0, 0, 0, 0],
        [0, 7, 0, 0, 9, 0, 2, 0, 0],
        [0, 5, 0, 0, 0, 7, 0, 0, 0],
        [0, 0, 0, 0, 4, 5, 7, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 3, 0],
        [0, 0, 1, 0, 0, 0, 0, 6, 8],
        [0, 0, 8, 5, 0, 0, 0, 1, 0],
        [0, 9, 0, 0, 0, 0, 4, 0, 0]
    ]
0s represent the numbers to be found.""")
        return None
        
    for i, row in enumerate(board):
        row = list(map(str, row))
        row.insert(6, '|')
        row.insert(3, '|')
        r = ' '.join(row).replace('0', ' ')

        print(r)
        
        if i in (2, 5):
            print('----------------------')


def find_zero(board: List[List[int]]) -> List[int] | None:
    for r, row in enumerate(board):
        for c, col in enumerate(row):
            if col == 0:
                return [r, c]
    return None


def is_valid(board: List[List[int]], row: int, col: int, value: int) -> bool:
    # Check the value is not already in the row
    if value in board[row]:
        return False

    # Check the value is not already in the column
    if any(value == board[i][col] for i in range(0,9)):
        return False

    # Check the value is not already in the 3*3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == value:
                return False
    
    return True

 
def solve(board: List[List[int]]) -> bool:
    next_zero = find_zero(board)
    if not next_zero:
        return True
    else:
        row, col = next_zero

    for i in range(1, 10):
        if is_valid(board, row, col, i):
            board[row][col] = i
            if solve(board):
                return True
            board[row][col] = 0
    return False


def solve_sudoku(board: List[List[int]]) -> List[List[int]] | None:
    res = copy.deepcopy(board)

    if solve(res):
        return res
    else:
        return None


def is_sudoku_correct(board: List[List[int]]) -> bool:
    def check_duplicates(nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num != 0 and num in seen:
                return False
            seen.add(num)
        return True

    for row in board:
        if not check_duplicates(row):
            return False

    for col in range(9):
        if not check_duplicates([board[row][col] for row in range(9)]):
            return False

    for i in range(3):
        for j in range(3):
            subgrid = [board[m][n] for m in range(3*i, 3*i+3) for n in range(3*j, 3*j+3)]
            if not check_duplicates(subgrid):
                return False

    return True
    
