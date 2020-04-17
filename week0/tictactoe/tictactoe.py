"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]
    ]


def is_empty(board):
    """
    Checks whether a board is empty.
    """
    return board == [
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]
    ]


def get_count(board):
    items = [item for row in board for item in row]
    ret = {'X': 0, 'O': 0}
    for item in items:
        if item in ret:
            ret[item] += 1
        else:
            ret[item] = 1
    return ret


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if is_empty(board):
        return 'X'
    else:
        counts = get_count(board)
        if counts['X'] > counts['O']:
            return 'O'
        elif counts['X'] == counts['O']:
            return 'X'


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return [(i, j) for i in range(3) for j in range(3) if not board[i][j]]


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    plyr = player(board)
    result = copy.deepcopy(board)

    if not result[action[0]][action[1]]:
        result[action[0]][action[1]] = plyr
        return result
    else:
        raise ValueError('Invalid action or board')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in board:
        if row[0] and row[1] and row[2]:
            if row[0] == row[1] == row[2]:
                return row[0]

    for i in range(3):
        if board[0][i] and board[1][i] and board[2][i]:
            if board[0][i] == board[1][i] == board[2][i]:
                return board[0][i]

    if board[0][0] and board[1][1] and board[2][2]:
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]

    if board[0][2] and board[1][1] and board[2][0]:
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    elif len([item for row in board for item in row if item]) == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == 'X':
        return 1
    elif w == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    returns:
        action: (i, j)
        The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    """
    if terminal(board):
        return None

    def minimax_func(plyr):
        if plyr == 'X':
            return max
        elif plyr == 'O':
            return min

    def get_scores(board, memo=None):
        if terminal(board):
            return utility(board)

        plyr = player(board)
        A = list(actions(board))

        total_val = 0
        memo = set()

        for a in A:
            result_board = result(board, a)

            if str(result_board) not in memo:
                memo.add(str(result_board))
                total_val += get_scores(result_board, memo)

        return total_val
    """
    approach
        1. determine who's turn it is
        2. get available actions
        3. get the corresponding minimax func for the player
        4. for each action, determine value (sum of all possible consequences) and store index and action

        iteration
        - for each action, take the action and get the result board
        - if not terminal, recurse
        - if terminal, return score
    """

    A = list(actions(board))
    plyr = player(board)
    func = minimax_func(plyr)
    best = None
    scores = {}

    print(A)
    # shuffle order of A

    for a in A:
        result_board = result(board, a)
        score = get_scores(result_board)
        if not best:
            best = score
        else:
            best = func(best, score)
        scores[score] = a

    print(scores)
    return scores[best]
