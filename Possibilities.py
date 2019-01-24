
class PossibleMoves:
    def __init__(self,board,play,score,parent):
        self.board = board
        self.play = play
        self.score = score
        self.parent = parent
        self.compare = 0


class Depths:
    def __init__(self,depth,children):
        self.depth = depth
        self.children = children
        self.utility = 0
