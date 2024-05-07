
def did_I_win_2_down(player, board):
    # declare whether or not you won
    did_win = False
    # create the loop to itterate through the board.
    for i in range(len(board)):
        col_win = True
        for x in range(len(board[i])):
            col_win &= player == board[x][i]
        # print("\t", i, col_win, "or", did_win)
        did_win |= col_win

    return did_win


def did_I_win_down(player, board):
    all_win = False  # Boolean agregator
    for x in range(3):  # for each column
        did_win = True  # did win the column
        for i in range(3):  # for each row
            did_win &= player == board[i][x]
        all_win |= did_win

    return all_win


def print_2D_board(b):
    for i in range(len(b)):
        print(b[i])


def main():
    boards = [[["X", "O", "O"]] * 3,
              [["X", "O", "X"], ["O"] * 3, ["O", "X", "O"]],
              [["O", "O", "X"], ["O", "X", "O"], ["X", "O", "O"]],
              [["O", "O", "X"]] * 3]

    for b in boards:
        print_2D_board(b)
        print("X won?", did_I_win_down("X", b))
        print("O won?", did_I_win_down("O", b))

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
