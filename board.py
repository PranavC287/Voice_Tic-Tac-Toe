EMPTY = ""
PLAYER = "X"
AI = "O"

def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

def make_move(board, row, column, player):
    if board[row][column] == EMPTY:
        board[row][column] = player
        return True
    return False

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY: #checking row for winners
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY: #checking columns for winners
            return board[0][i]
        
    if board[0][0] == board[1][1] == board[2][2] != EMPTY: #checking top left to bottom right diagonal
            return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY: #checking bottom left to top right diagonal
            return board[0][2]

    return None #no winner

def is_full(board):
    return all(cell != EMPTY for row in board for cell in row)

def reset_board(board):
    for row in range(3):
        for column in range(3):
            board[row][column] = EMPTY




