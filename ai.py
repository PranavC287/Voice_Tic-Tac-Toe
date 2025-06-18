from board import PLAYER, AI, EMPTY, check_winner, is_full

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == PLAYER:
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = AI
                    score = minimax(board, False)
                    board[row][col] = EMPTY
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == EMPTY:
                    board[row][col] = PLAYER
                    score = minimax(board, True)
                    board[row][col] = EMPTY
                    best_score = min(score, best_score)
        return best_score

def get_best_move(board):
    best_score = -float("inf")
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                board[row][col] = AI
                score = minimax(board, False)
                board[row][col] = EMPTY

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move
