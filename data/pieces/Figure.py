from data.board.Board import board


class Figure:
    def __init__(self, field):
        self.field = field
        self.available_moves_list = []
        self.position_data = self.get_position()

    def get_position(self):
        letter = self.field[0]
        number = int(self.field[1])
        letters = list(board.board.keys())
        letter_index = letters.index(letter)
        letter_row_right = None
        letter_row_left = None

        if letter_index < 7:
            letter_row_right = letters[letter_index + 1]
        if letter_index > 0:
            letter_row_left = letters[letter_index - 1]

        neighbours_rows = [letter, letter_row_left, letter_row_right]

        return {
            "letters": letters,
            "letter": letter,
            "number": number,
            "neighbours_rows": neighbours_rows,
            "letter_index": letter_index,
        }

    def list_available_moves(self):
        return self.available_moves_list

    def validate_move(self, dest_field):
        if dest_field in self.available_moves_list:
            return True
        else:
            return False
