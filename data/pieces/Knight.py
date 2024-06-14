from data.pieces.Figure import Figure
from data.board.Board import board


class Knight(Figure):
    def __init__(self, field):
        super().__init__(field)
        self.knight_available_moves()

    def knight_available_moves(self):
        # Hardcoded all possible moves for knight
        knight_possible_moves = [
            f"{board.get_letter_index(self.position_data['letter']) - 2}{self.position_data['number'] - 1}",
            f"{board.get_letter_index(self.position_data['letter']) - 2}{self.position_data['number'] + 1}",
            f"{board.get_letter_index(self.position_data['letter']) - 1}{self.position_data['number'] - 2}",
            f"{board.get_letter_index(self.position_data['letter']) + 1}{self.position_data['number'] - 2}",
            f"{board.get_letter_index(self.position_data['letter']) - 1}{self.position_data['number'] + 2}",
            f"{board.get_letter_index(self.position_data['letter']) + 1}{self.position_data['number'] + 2}",
            f"{board.get_letter_index(self.position_data['letter']) + 2}{self.position_data['number'] + 1}",
            f"{board.get_letter_index(self.position_data['letter']) + 2}{self.position_data['number'] - 1}",
        ]

        # Every incorrect move don't add to self.available_moves_list
        for possible_move in knight_possible_moves:
            try:
                valid_letter = self.position_data["letters"][int(possible_move[0])]
                if 0 < int(possible_move[1]) < 9:
                    self.available_moves_list.append(
                        f"{valid_letter}{possible_move[1]}"
                    )
            except (IndexError, ValueError):
                pass
