"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    [COMPLETED]Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    [COMPLETED]Returns player who has the next turn on a board.
    """
    emptyCells = 0 
    for row in board: 
        for element in row: 
            emptyCells = emptyCells + 1 if element is EMPTY else emptyCells

    return X if emptyCells % 2 == 1 else O


def actions(board):
    """
    [COMPLETED]Returns set of all possible actions (i, j) available on the board.
    """
    possibleMoves = set()
    for i in range(len(board)): 
        for j in range(len(board[0])): 
            if board[i][j] is EMPTY: 
                possibleMoves.add((i, j))
    
    return possibleMoves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoardState = deepcopy(board)
    if newBoardState[action[0]][action[1]] is not EMPTY: 
        raise Exception('Block already filled')
    
    newBoardState[action[0]][action[1]] = player(newBoardState)
    return newBoardState 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range (len(board)):
        if board[1][1] == board[2][2] == board[0][0]:
            return board[1][1]
        elif board[2][0] == board[1][1] == board[0][2]:
            return board[1][1]
        elif board[i][0] == board[i][1] == board[i][2]:
            return board[i][1]
        elif board[0][i] == board[1][i] == board[2][i]:
            return board[1][i]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None: 
        return True
    
    for row in board: 
        for element in row: 
            if element is EMPTY: 
                return False
    
    return True
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) is X: 
        return 1
    elif winner(board) is O: 
        return -1 
    elif winner(board) is None: 
        return 0 


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    
