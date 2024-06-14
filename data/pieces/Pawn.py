from data.pieces.Figure import Figure


class Pawn(Figure):
    def __init__(self, field):
        super().__init__(field)
        self.pawn_available_moves()

    def pawn_available_moves(self):
        if self.position_data["number"] + 1 <= 8:
            self.available_moves_list.append(
                f"{self.position_data['letter']}{self.position_data['number'] + 1}"
            )
        if self.position_data["number"] == 2:
            self.available_moves_list.append(
                f"{self.position_data['letter']}{self.position_data['number'] + 2}"
            )
