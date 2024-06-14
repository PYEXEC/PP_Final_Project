from data.pieces.Rook import Rook
from data.pieces.Bishop import Bishop


class Queen(Rook, Bishop):
    def __init__(self, field):
        super().__init__(field)
        self.queen_available_moves()

    def queen_available_moves(self):
        super().rook_available_moves()
        super().bishop_available_moves()
        self.available_moves_list = set(self.available_moves_list)
