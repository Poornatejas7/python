def is_valid(puzzle, guess, row, col):
    """Check if a number is valid at a given position in the Sudoku grid."""
    # Check the row
    if guess in puzzle[row]:
        return False

    # Check the column
    if guess in (puzzle[i][col] for i in range(9)):
        return False

    # Check the 3x3 grid
    start_row, start_col = (row // 3) * 3, (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if puzzle[i][j] == guess:
                return False

    return True

def find_next_empty(puzzle):
    """Find the next empty cell in the Sudoku grid."""
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:
                return row, col
    return None, None

def print_puzzle(puzzle):
    """Print the Sudoku puzzle in a formatted grid."""
    for i, row in enumerate(puzzle):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Print horizontal separator
        print(" | ".join(" ".join(str(puzzle[i][j] if puzzle[i][j] != 0 else ".") 
                                   for j in range(k, k + 3)) for k in range(0, 9, 3)))
    print("\n")

def sudoku_solver(puzzle, visualize=False):
    """Solve the Sudoku puzzle using backtracking."""
    # Find the next empty cell
    row, col = find_next_empty(puzzle)
    if row is None:  # Puzzle is solved
        return True, puzzle

    for guess in range(1, 10):  # Try numbers 1-9
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess

            if visualize:
                print(f"Trying {guess} at ({row}, {col})")
                print_puzzle(puzzle)

            # Recursively attempt to solve the rest of the puzzle
            solved, solved_puzzle = sudoku_solver(puzzle, visualize)
            if solved:
                return True, solved_puzzle

        # Undo the guess
        puzzle[row][col] = 0

    return False, puzzle

def validate_puzzle(puzzle):
    """Validate the input Sudoku puzzle for correctness."""
    if not (isinstance(puzzle, list) and len(puzzle) == 9):
        return False
    for row in puzzle:
        if not (isinstance(row, list) and len(row) == 9):
            return False
        if not all(isinstance(cell, int) and 0 <= cell <= 9 for cell in row):
            return False
    return True

# Input Sudoku Puzzle
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

if validate_puzzle(puzzle):
    print("Input Sudoku Puzzle:")
    print_puzzle(puzzle)

    solved, solution = sudoku_solver(puzzle, visualize=True)
    if solved:
        print("Solved Sudoku Puzzle:")
        print_puzzle(solution)
    else:
        print("No solution exists for the given puzzle.")
else:
    print("Invalid Sudoku puzzle input.")
