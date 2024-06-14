from data.pieces.Figure import Figure
from data.board.Board import board


class Bishop(Figure):
    def __init__(self, field):
        super().__init__(field)
        self.bishop_available_moves()

    def bishop_available_moves(self):
        for letter in self.position_data["letters"]:
            for i in range(1, 9):
                dx = abs(
                    board.get_letter_index(letter)
                    - board.get_letter_index(self.position_data["letter"])
                )
                dy = abs(i - self.position_data["number"])
                if dx == dy and dx > 0:
                    self.available_moves_list.append(f"{letter}{i}")
