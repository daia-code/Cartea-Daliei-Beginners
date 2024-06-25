from board import initialize_board, print_board, make_move, check_winner, is_board_full

def switch_player(player):
    return 'O' if player == 'X' else 'X'

def play_game():
    board = initialize_board()
    current_player = 'X'
    while True:
        print_board(board)
        print(f"Jucătorul {current_player}, este rândul tău.")
        try:
            row = int(input("Introduce rândul (0, 1, 2): "))
            col = int(input("Introduce coloana (0, 1, 2): "))
        except ValueError:
            print("Introduceți un număr valid.")
            continue

        if not make_move(board, row, col, current_player):
            print("Mutare invalidă, încercați din nou.")
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f"Jucătorul {current_player} a câștigat!")
            break

        if is_board_full(board):
            print_board(board)
            print("Remiză! Tabla este completă.")
            break

        current_player = switch_player(current_player)
