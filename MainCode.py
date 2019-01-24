from MinMax import *

def print_board(board):
    for row in board:
        for column in row:
            print(column,end=" ")
        print("\n")

def size_input():
    width = int(input("Enter board width:"))
    height = int(input("Enter board height:"))

    if (width < 4) or (height < 4):
        print("Size should be atleast 4x4")
        size_input()

    return width,height

def create_board(width, height):

    created_board = np.zeros((height,width)).astype(str)
    created_board[:] = '.'

    nums = np.arange(1,width+1)
    created_board = np.vstack((created_board,nums))

    return created_board

def check_four(board):

    for row in board:
        for k,g in groupby(row):
            group = list(g)

            if group == ['X','X','X','X']:
                return True


            elif group == ['O','O','O','O']:
                return True

    return False

def check_diag(board):
    diag_lists = list(diags(board))

    for group in diag_lists:
        if group == ['X','X','X','X']:
            return True

        elif group == ['O','O','O','O']:
            return True

    return False


def check_win(board):

    horizontal_four = check_four(board)

    board = board.T

    vertical_four = check_four(board)

    diag_four = check_diag(board)
    reverse_board = np.flip(board,0)
    reverse_diag_four = check_diag(reverse_board)

    if horizontal_four or vertical_four or diag_four or reverse_diag_four:
        return True
    else:
        return False



if __name__ == "__main__":

    board_width, board_height = size_input()
    depth = int(input("Enter depth:"))

    board = create_board(board_width,board_height)
    score = calculate_score(board,"X")
    print_board(board)
    game = PossibleMoves(board,None,score,None)

    while check_win(game.board)==False:
        min_play = int(input("Your turn:"))
        game.board = min_update_board(game.board,min_play)
        print_board(game.board)

        if check_win(game.board):
            break

        print("-------------------------------------")

        max_play = min_max(game,depth)
        game.board = max_update_board(game.board,max_play)
        print_board(game.board)
        print("-------------------------------------")

    print("Game Over!")


