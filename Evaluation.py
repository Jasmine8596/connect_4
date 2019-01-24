from itertools import groupby
import numpy as np

def calculate_score(board,player_sign):
    horizontal_score = horizontal_check(board,player_sign)
    vertical_score = vertical_check(board,player_sign)
    diagonal_score = diagonal_check(board,player_sign)

    total_score = horizontal_score + vertical_score + diagonal_score
    return total_score


def horizontal_check(board,player_sign):

    my_four = 0
    my_three = 0
    my_two = 0
    opp_four = 0
    opp_three = 0
    opp_two = 0

    for row in board:
        for k,g in groupby(row):
            group = list(g)

            if player_sign == "X":

                if group == ['X','X','X','X']:
                    my_four += 1

                elif group == ['X','X','X']:
                    my_three += 1

                elif group == ['X','X']:
                    my_two += 1

            elif player_sign == "O":

                if group == ['O','O','O','O']:
                    opp_four += 1

                elif group == ['O','O','O']:
                    opp_three += 1

                elif group == ['O','O']:
                    opp_two += 1

    horizontal_score = my_four*10000 + my_three*1000 + my_two*100 + \
                       (-opp_four*100000 - opp_three*1000 - opp_two*100)

    return horizontal_score

def vertical_check(board,player_sign):
    board = board.T
    vertical_score = horizontal_check(board,player_sign)

    return vertical_score

def diagonal_check(board,player_sign):
    diag_score = check_diagonal_score(board,player_sign)
    reverse_board = np.flip(board,0)
    reverse_diag_score = check_diagonal_score(reverse_board,player_sign)

    return (diag_score+reverse_diag_score)

def check_diagonal_score(board,player_sign):
    my_four = 0
    my_three = 0
    my_two = 0
    opp_four = 0
    opp_three = 0
    opp_two = 0

    diag_lists = list(diags(board))

    for group in diag_lists:

        if player_sign == "X":

            if group == ['X','X','X','X']:
                my_four += 1

            elif group == ['X','X','X']:
                my_three += 1

            elif group == ['X','X']:
                my_two += 1

        elif player_sign == "O":

            if group == ['O','O','O','O']:
                opp_four += 1

            elif group == ['O','O','O']:
                opp_three += 1

            elif group == ['O','O']:
                opp_two += 1

    diag_score = my_four*10000 + my_three*1000 + my_two*100 + \
                 (-opp_four*100000 - opp_three*1000 - opp_two*100)

    return diag_score

def diags(mat):
    width, height = len(mat[0]), len(mat)
    def diag(sx, sy):
        for x, y in zip(range(sx, height), range(sy, width)):
            yield mat[x][y]
    for sx in range(height):
        yield list(diag(sx, 0))
    for sy in range(1, width):
        yield list(diag(0, sy))


