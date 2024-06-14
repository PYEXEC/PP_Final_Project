from data.pieces.Figure import Figure


class Rook(Figure):
    def __init__(self, field):
        super().__init__(field)
        self.rook_available_moves()

    def rook_available_moves(self):
        for letter in self.position_data["letters"]:
            for i in range(1, 9):
                if f"{letter}{i}" != self.field:
                    if (
                        i == self.position_data["number"]
                        or letter == self.position_data["letter"]
                    ):
                        self.available_moves_list.append(f"{letter}{i}")
