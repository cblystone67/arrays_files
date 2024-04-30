
def did_I_win_2_down(player, board):
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    return False


def main():
    print(did_I_win_2_down("X", [['O', 'O', 'X'],
                                 ['O', 'X', 'O'],
                                 ['X', 'O', 'O']]))


print(did_I_win_2_down("O", [['O', 'O', 'X'],
                             ['O', 'X', 'O'],
                             ['X', 'O', 'O']]))
print(did_I_win_2_down("X", [['O', 'O', 'X'],
                             ['O', 'O', 'O'],
                             ['O', 'O', 'O']]))
print(did_I_win_2_down("O", [['O', 'O', 'X'],
                             ['O', 'O', 'O'],
                             ['O', 'O', 'O']]))


if __name__ == "__main__":
    main()
