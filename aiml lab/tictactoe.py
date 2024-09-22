import math

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-" * 13)

# Function to check if the current board has a winner
def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

# Function to check if there are any empty spots left
def is_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Minimax algorithm to determine the best move for the AI
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'O':  # AI win
        return 1
    elif winner == 'X':  # Player win
        return -1
    elif is_full(board):  # Draw
        return 0

    if is_maximizing:
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '
                    best_score = min(score, best_score)
        return best_score

# Function for the AI to make a move using Minimax
def ai_move(board):
    best_score = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    if best_move:
        board[best_move[0]][best_move[1]] = 'O'

# Function for the player to make a move
def player_move(board):
    while True:
        move = input("Enter your move (row col): ").split()
        if len(move) != 2:
            print("Please enter two numbers (row and column).")
            continue

        row, col = int(move[0]) - 1, int(move[1]) - 1

        if row not in range(3) or col not in range(3):
            print("Invalid position. Try again.")
        elif board[row][col] != ' ':
            print("Position already taken. Try again.")
        else:
            board[row][col] = 'X'
            break

# Main function to play Tic-Tac-Toe
def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe!")
    print("You are X, AI is O")
    print_board(board)

    while True:
        # Player's move
        player_move(board)
        print_board(board)

        if check_winner(board):
            print("You win!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        # AI's move
        ai_move(board)
        print_board(board)\

        if check_winner(board):
            print("AI wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
