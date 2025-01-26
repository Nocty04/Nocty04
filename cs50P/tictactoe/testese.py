from tictactoe import minimax

# Define the board state
board = [
    [None, None, "X"],  # O has a threat here
    ["X", None, "O"],  # X is placing here
    [None, None, "O"]   # X can win by placing at (2, 0)
]
# Print the result of the minimax function
print(minimax(board))
