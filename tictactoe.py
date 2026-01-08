"""
Tic Tac Toe Player
"""

import math as m
import copy as c

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY,EMPTY,EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.

    """

    filled_spaces = 9 - len(actions(board))

    if filled_spaces % 2 == 0:
        return "X"
    else:
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    possible_actions = set()

    for i in range(0, 3):
        for j in range(0, 3):

            if board[i][j] is None:
                possible_actions.add((i, j))


    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    new_board = c.deepcopy(board)

    if new_board[action[0]][action[1]] != None:
        raise Exception("action invalid because space is already filled")
    else:
        if player(board) == "X":
            new_board[action[0]][action[1]] = "X"
            return new_board

        else:
            new_board[action[0]][action[1]] = "O"
            return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    if terminal(board) == True:
        if utility(board) == 1:
            return "X"
        elif utility(board) == -1:
            return "O"
        elif utility(board) == 0:
            return 'Nobody'
    else:
        return None



    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # check for horizontal 3-in-a-row
    for i in range(0,3):
        if board[i][0] != None:
            expected = board[i][0]
            horizontal_row = True
            for j in range(1,3):
                if board[i][j] != expected:
                    horizontal_row = False
            if horizontal_row: return True
    
    # check for vertical 3-in-a-row
    for i in range(0,3):
        if board[0][i] != None:
            expected = board[0][i]
            vertical_row = True
            for j in range(1,3):
                if board[j][i] != expected:
                    vertical_row = False
            if vertical_row: return True
    
    # check for diagonal (starting from top-left)
    if board[0][0] != None:
        expected = board[0][0]
        diagonal_l = True
        for i in range(1,3):
            if board[i][i] != expected:
                diagonal_l = False
        if diagonal_l: return True
    
    # check for diagonal (starting from top-right)
    if board[0][2] != None:
        expected = board[0][2]
        diagonal_r = True
        for i in range(1,3):
            if board[i][-1*i+2] != expected:
                diagonal_r = False
        if diagonal_r: return True
    
    everything_filled = True 
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] == None:
                everything_filled = False 
    if everything_filled: return True

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    if terminal(board):
        #checking for horizontal 3-in-a-row  
        for i in range(0,3):
            expected = board[i][0]
            three_in_a_row = True
            for j in range(1,3):
                if board[i][j] != expected:
                    three_in_a_row = False 
            if three_in_a_row: 
                if expected == 'X':
                    return 1
                elif expected == 'O':
                    return -1
        
        #checking for vertical 3-in-a-row  
        for i in range(0,3):
            expected = board[0][i]
            three_in_a_row = True
            for j in range(1,3):
                if board[j][i] != expected:
                    three_in_a_row = False
            if three_in_a_row: 
                if expected == 'X':
                    return 1
                elif expected == 'O':
                    return -1

        #checking for diagonal 3-in-a-row (starting top-left)    
        expected = board[0][0]
        three_in_a_row = True
        for i in range(1,3):
            if board[i][i] != expected:
                three_in_a_row = False 
        if three_in_a_row == True:
            if expected == 'X':
                return 1
            if expected == 'O':
                return -1
        
        #checking for diagonal 3-in-a-row (starting top-right)    
        expected = board[0][2]
        three_in_a_row = True
        for i in range(1,3):
            if board[i][-1*i+2] != expected:
                three_in_a_row = False 
        if three_in_a_row == True:
            if expected == 'X':
                return 1
            if expected == 'O':
                return -1

        return 0 
    else:
        return 0 

    
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    possible_moves = actions(board)
    utility_move = dict()
    
    for i in possible_moves:
        result_state = result(board, i)
        next_turn = True if player(result_state) == "X" else False 
        current_util = actual_minimax(result_state, next_turn)
        utility_move.update({current_util:i})
    
    list_form = [a for a in utility_move.keys()]
    turn = True if player(board) == "X" else False

    if turn:
        return utility_move[max(tuple(list_form))]
    else:
        return utility_move[min(tuple(list_form))]


def actual_minimax(board, max_player):
    """
    different from the previous minimax function - this one actually does the evaluations of each state through recursion
    """
    possible_states = []
    for i in actions(board):
        possible_states.append(result(board, i))

    if terminal(board): 
        return utility(board)
    
    if max_player:
        maxEval = -m.inf
        for i in possible_states:
            eval = actual_minimax(i, False)
            maxEval = max(maxEval, eval)
        return maxEval
    
    else:
        minEval = +m.inf
        for i in possible_states:
            eval = actual_minimax(i, True)
            minEval = min(minEval, eval)
        return minEval




        


    

