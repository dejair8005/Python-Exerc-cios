def draw_board(board):
    print('-------------')
    for i in range(3):
        print('|', board[i][0], '|', board[i][1], '|', board[i][2], '|')
        print('-------------')


def check_win(board):
    # Check horizontal
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            return True

    # Check vertical
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            return True

    # Check diagonal
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True

    return False


def play_game():
    board = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    current_player = 'X'
    game_over = False

    while not game_over:
        draw_board(board)

1        # Get player input
        row = int(raw_input(f'Jogador {current_player}, escolha a linha (0-2): '))
        col = int(raw_input(f'Jogador {current_player}, escolha a coluna (0-2): '))

        # Update board
        if board[row][col] == '-':
            board[row][col] = current_player
        else:
            print('Essa posição já está ocupada. Tente novamente.')
            continue

        # Check for winner or tie
        if check_win(board):
            draw_board(board)
            print(f'Jogador {current_player} venceu!')
            game_over = True
        elif all('-' not in row for row in board):
            draw_board(board)
            print('Empate!')
            game_over = True

        # Switch player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'


play_game()
