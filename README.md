# sudoku_solver
Simple Sudoku solver with helpers and a wrapper

The board format is the following :
  tList[List[int]]
  9 * 9
  0 <= int < 10
  0s represent the numbers to be found.
  Example :
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

2 boards are embeded, named "board1" and "board2".

Functions :
  solve_sudoku(board: List[List[int]]) -> List[List[int]] | None
    Solve the sudoku, without modifying the initial board.
    Return the solved sudoku if it could be solved.
    Return None otherwise.
  
  solve(board: List[List[int]]) -> bool
    Solve the sudoku in-place.
    Return True if the udoku could be solved.
    return False otherwise.
  
  is_valid(board: List[List[int]], row: int, col: int, value: int) -> bool:
    Return True if value can be placed at the the (row, col) coordinates.
    Return None otherwise.
  
  find_zero(board: List[List[int]]) -> List[int]
    Return the coordinates of the next 0 in the grid.
    If the grid is complete, return None.
  
  print_board(board: List[List[int]] | None) -> None
    Print the board if the format is correct.
    Print a message indicating the board is empty if board is None or []
    Print indication about the format if not correct

  is_sudoku_correct(board: List[List[int]]) -> bool
    Verify if a completed sudoku is valid, and return True if so.
    Return False otherwise.
