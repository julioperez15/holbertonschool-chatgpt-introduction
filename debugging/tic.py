def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows and columns for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return True
    
    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    
    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while not check_winner(board):
        print_board(board)
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            if not (0 <= row < 3 and 0 <= col < 3):
                print("Invalid input. Row and column should be between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            player = "O" if player == "X" else "X"
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print_board(board)

tic_tac_toe()