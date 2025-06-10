"""
Tic Tac Toe Player
"""

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


def whoseTurn(board):
    x_count = sum(row.count(X) for row in board)
    o_count = sum(row.count(O) for row in board)
    if x_count > o_count:
        return O # O's turn if X has played more
    else:
        return X # X starts first


def allPossibleMoves(board):
    # Returns a set of all possible actions (i, j) available on the board.
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                actions.add((i, j))
    return actions


def resultingBoardFromMove(board, action):
    # Returns the board that results from making a move (i, j) on the board.
    i, j = action
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: Cell is already occupied.")
    new_board = [row[:] for row in board]  # Create a copy of the board
    new_board[i][j] = whoseTurn(board)  # Place the current player's mark
    return new_board


def winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY: # Check rows
            # return the value of the first item in the row if all three items are equal
            return board[i][0] 
        
        if board[0][i] == board[1][i] == board[2][i] != EMPTY: # Check columns
            # return the value of the first item in the column if all three items are equal
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] != EMPTY: # Check main diagonal
        # return the value of the first item in the main diagonal if all three items are equal
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != EMPTY: # Check anti-diagonal
        # return the value of the first item in the anti-diagonal if all three items are equal
        return board[0][2]
    
    return None  # No winner yet
 

def terminal(board):
    # Check if the game is over
    if winner(board) is not None:
        return True #We have a winner 
    if all(cell is not EMPTY for row in board for cell in row):
        return True # Board is full so its a draw
    return False # no Winner

def gameResult(board):
    # Returns 1 if X has won, -1 if O has won, and 0 otherwise.
    win = winner(board)
    if win == X:
        return 1 # X has won
    elif win == O:
        return -1 # O has won
    else:
        return 0  # No winner, or it's a draw


def minimax(board):
    #return the action that leads to the best outcome for the current player
    if terminal(board):
        return None  # Game is over, no action to take
    if whoseTurn(board) == X:
        # X is maximizing player
        value, action = max_value(board)
        return action
    else:
        # O is minimizing player
        value, action = min_value(board)
        return action
    
def max_value(board):
    if terminal(board): # is the game over?
        return gameResult(board), None  # return who won or return None if its a draw
    v = -math.inf # Initialize v to negative infinity for maximizing player
    best_action = None
    for action in allPossibleMoves(board): # For all possile actions
        new_board = resultingBoardFromMove(board, action) # Get the new board after making a possible action
        min_val, _ = min_value(new_board) # Get the min value from this new board
        if min_val > v: 
            v = min_val # Update v to the new min value if its greater than current v
            best_action = action # Update the best action to the current action
    return v, best_action #return the best value and action

def min_value(board):
    if terminal(board): # is the game over?
        return gameResult(board), None  # return who won or return None if its a draw
    v = math.inf # Initialize v to positive infinity for minimizing player
    best_action = None
    for action in allPossibleMoves(board): # For all possile actions
        new_board = resultingBoardFromMove(board, action) # Get the new board after making a possible action
        max_val, _ = max_value(new_board) # Get the max value from this new board
        if max_val < v:
            v = max_val # Update v to the new max value if its less than current v
            best_action = action # Update the best action to the current action
    return v, best_action #return the best value and action

