def is_safe(board, row, col):
    """
    Check if placing a queen at (row, col) is safe.
    board[row] = column index where queen is placed in that row.
    """
    for prev_row in range(row):
        placed = board[prev_row]
        # Same column
        if placed == col:
            return False
        # Same diagonal
        if abs(prev_row - row) == abs(placed - col):
            return False
    return True


def solve_n_queens(n):
    """
    Solve the N-Queens problem and return all solutions.
    Each solution is represented as a list of column positions.
    """
    board = [-1] * n  # -1 means no queen placed in that row
    solutions = []

    def backtrack(row):
        if row == n:
            # Found a valid solution
            solutions.append(board.copy())
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Backtrack

    backtrack(0)
    return solutions


def print_solutions(solutions, n):
    """
    Print the board representation of each solution.
    """
    for idx, sol in enumerate(solutions, start=1):
        print(f"Solution {idx}:")
        for row in range(n):
            line = ["Q" if sol[row] == col else "." for col in range(n)]
            print(" ".join(line))
        print()


if __name__ == "__main__":
    try:
        n = int(input("Enter the value of N (>=4 recommended): "))
        if n <= 0:
            print("N must be a positive integer.")
        else:
            solutions = solve_n_queens(n)
            print(f"Total solutions for {n}-Queens: {len(solutions)}")
            print_solutions(solutions, n)
    except ValueError:
        print("Invalid input. Please enter an integer.")