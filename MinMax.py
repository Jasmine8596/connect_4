from Evaluation import *
from Possibilities import *

def min_update_board(board,min_play):
    extract = board[:,min_play-1]
    extract = extract[::-1]

    count = board.shape[0] - 1
    for element in extract:
        if element == ".":
            board[count,min_play-1] = "O"
            return board
        count = count - 1

def max_update_board(board,max_play):
    extract = board[:,max_play-1]
    extract = extract[::-1]

    count = board.shape[0] - 1
    for element in extract:
        if element == ".":
            board[count,max_play-1] = "X"
            return board
        count = count - 1

from copy import deepcopy

def create_children(game,player_sign):
    children = np.array([])

    for play in range(0,game.board.shape[1]):
        child_board = deepcopy(game.board)
        if player_sign == "X":
            child_board = max_update_board(child_board,play)
            score = calculate_score(child_board,"X")
            child = PossibleMoves(child_board,play,score,game)
        elif player_sign == "O":
            child_board = min_update_board(child_board,play)
            score = calculate_score(child_board,"O")
            child = PossibleMoves(child_board,play,score,game)
        children = np.append(children,child)

    return children

def min_max(game,depth):
    depths = np.array([])
    children = create_children(game,"X")
    create_depth = Depths(0,children)

    depths = np.append(depths,create_depth)

    for depth_count in range(1,depth):
        selected_depth = depths[-1]
        all_children = np.array([])

        for child in selected_depth.children:

            if (depth_count)%2 == 0:
                children = create_children(child,"X")

            elif (depth_count)%2 != 0:
                children = create_children(child,"O")

            all_children = np.append(all_children,children)
        create_depth = Depths(depth_count,all_children)
        depths = np.append(depths,create_depth)

    for depth_index in range(depth-1,-1,-1):
        current_depth = depths[depth_index]
        parent_depth = depths[depth_index-1]

        if current_depth.depth%2 == 0:
            current_depth.utility = -10000
            parent_depth.utility = 10000

        elif current_depth.depth%2 != 0:
            current_depth.utility = 10000
            parent_depth.utility = -10000

    for depth_index in range(depth-1,-1,-1):
        current_depth = depths[depth_index]
        parent_depth = depths[depth_index-1]

        if current_depth.depth%2 == 0:
            start_point = 0
            end_point = 9
            for move in parent_depth.children:
                selected_children = current_depth.children[start_point:end_point]

                max_score = current_depth.utility
                for child in selected_children:
                    if max_score < child.score:
                        max_score = child.score

                move.compare = max_score
                start_point = end_point
                end_point += 9


        elif current_depth.depth%2 != 0:
            start_point = 0
            end_point = 9
            for move in parent_depth.children:
                selected_children = current_depth.children[start_point:end_point]

                min_score = current_depth.utility
                for child in selected_children:
                    if min_score > child.score:
                        min_score = child.score

                move.compare = min_score
                start_point = end_point
                end_point += 9

    max_score = depths[0].children[0].compare
    play = depths[0].children[0].play
    for child in depths[0].children:
        if max_score < child.compare:
            max_score = child.compare
            play = child.play

    return play