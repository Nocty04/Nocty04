"""
Tic Tac Toe Player
"""
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    start = initial_state()
    x = 0
    o = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                x += 1
            elif board[i][j] == O:
                 o += 1
    if board == start:
        return X
    elif x > o:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                available_actions.add((i,j))
            else:
                pass

    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Impossible")

    new_board = deepcopy(board)

    i, j = action
    new_board[i][j] = player(board)

    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winner_sets = [[(0, 0), (0, 1), (0, 2)],  # Horizontal row 0
                    [(1, 0), (1, 1), (1, 2)],  # Horizontal row 1
                    [(2, 0), (2, 1), (2, 2)],  # Horizontal row 2
                    [(0, 0), (1, 0), (2, 0)],  # Vertical column 0
                    [(0, 1), (1, 1), (2, 1)],  # Vertical column 1
                    [(0, 2), (1, 2), (2, 2)],  # Vertical column 2
                    [(0, 0), (1, 1), (2, 2)],  # Diagonal top-left to bottom-right
                    [(0, 2), (1, 1), (2, 0)]]


    for lists in winner_sets:
        marks = [board[x][y] for x, y in lists]
        if all(mark == marks[0] for mark in marks) and marks[0] != EMPTY:
            return marks[0]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or len(actions(board)) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def max_result(board):
    #helper

    if terminal(board):
        return utility(board)

    v = -math.inf
    for action in actions(board):
        v = max(v, min_result(result(board,action)))
    return v

def min_result(board):
    if terminal(board):
        return utility(board)

    v = math.inf
    for action in actions(board):
        v = min(v, max_result(result(board,action)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return None

    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_result(result(board, action)), action])
        print(plays)
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]


    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([min_result(result(board, action)), action])
        print(plays)
        return sorted(plays, key=lambda x: x[0])[0][1]



