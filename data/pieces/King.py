from data.pieces.Figure import Figure


class King(Figure):
    def __init__(self, field):
        super().__init__(field)
        self.king_available_moves()

    def king_available_moves(self):
        for char in self.position_data["neighbours_rows"]:
            for i in range(
                self.position_data["number"] - 1, self.position_data["number"] + 2
            ):
                if f"{char}{i}" != self.field and char is not None:
                    self.available_moves_list.append(f"{char}{i}")
