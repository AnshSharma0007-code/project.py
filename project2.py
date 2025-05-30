def print_board(board):
    print("\n")
    print("Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    print("Current Board:")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_winner(board, player):
    winning_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for pos in winning_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(space != ' ' for space in board)

def get_player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if move <1 or move >9:
                print("Invalid input. Enter a number between 1 and 9.")
                continue
            if board[move-1] != ' ':
                print("That position is already taken. Choose another.")
                continue
            return move-1
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")

def main():
    print("Welcome to Tic Tac Toe!")
    while True:
        board = [' '] * 9
        current_player = 'X'

        while True:
            print_board(board)
            move = get_player_move(board, current_player)
            board[move] = current_player

            if check_winner(board, current_player):
                print_board(board)
                print(f"Congratulations! Player {current_player} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch player after every valid move
            if current_player == 'X':
                current_player = 'O'
            else:
                current_player = 'X'

        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
