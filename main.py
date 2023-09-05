board = [" " for _ in range(9)]
# board
def print_board():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
#check for win
def check_win():
    # rows
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] != " ":
            return True
    # columns
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] != " ":
            return True
    # diagonals
    if board[0] == board[4] == board[8] != " ":
        return True
    if board[2] == board[4] == board[6] != " ":
        return True
    return False
def check_tie():
    return " " not in board
current_player = "X"
while True:
    print_board()
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1
    if 0 <= move < 9 and board[move] == " ":
        board[move] = current_player
        if check_win():
            print_board()
            print(f"Player {current_player} wins!")
            break
        elif check_tie():
            print_board()
            print("It's a tie!")
            break
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Invalid moveTryagain.")