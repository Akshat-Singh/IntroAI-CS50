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
    bestMove = (0, 0)
    copyState = deepcopy(board)                         # 1. Copy the board into a temporary state 
    currPlayer = player(board)                          # 2. Determine the current player
    
    if currPlayer is X:                                 # 3. If the current player is 'X'
        score = -math.inf                                   # i) Set the score to -infinity
        possibleMoves = actions(copyState)                  # ii) Find all possible moves
        for move in possibleMoves:                          # iii) Iterate over all possible moves    
            resultantState = result(copyState, move)        # iv) Find the resultant state after applying the current move     
            bestScore = minimize(resultantState)            # v) Score will be the maximum of all the 
                                                                # scores returned from 'Os' optimal move
            if bestScore > score:                           # vi) If the best score is greater than currentScore
                score = bestScore                               # Store new values for score and bestmove
                bestMove = move
        
    else:                                               # 4. If the current player is 'O'
        score = math.inf                                    # i) Set the score to infinity
        possibleMoves = actions(copyState)                  # ii) Find all possible moves
        for move in possibleMoves:                          # iii) Iterate over all possible moves    
            resultantState = result(copyState, move)        # iv) Find the resultant state after applying the current move     
            bestScore = maximize(resultantState)            # v) Score will be the minimum of all the 
                                                                # scores returned from 'Xs' optimal move
            if bestScore < score:                           # vi) If the best score is greater than currentScore
                score = bestScore                               # Store new values for score and bestmove
                bestMove = move
    
    return bestMove                                     # Return the best move


def minimize(board):                                     
    if terminal(board):                                 # If the terminal state is reached, return the score of the board
        return utility(board)
    
    score = math.inf                                    # Pick a number that is greater than any other number 
    possibleMoves = actions(board)                      # Find a set of possible moves for the board
    for move in possibleMoves:                          # Iterate over the list
        resultant = result(board, move)                 # Find the resultant from the current move
        score = min(score, maximize(resultant))         # Minimize the score obtained from X's optimal move
    return score

    
def maximize(board): 
    if terminal(board):                                 # If the terminal state is reached, return the utility score of the board
        return utility(board)
    
    score = -math.inf                                   # Set score to the smallest possible number
    possibleMoves = actions(board)                      # Find all possible moves for the current state
    for move in possibleMoves:                          # Iterate over all possible moves
        resultant = result(board, move)                 # Find the resultant from the current move
        score = max(score, minimize(resultant))         # Maximize the score obtained from O's optimal moves
    return score