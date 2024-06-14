from string import ascii_lowercase


class Board:
    def __init__(self):
        self.board = {}
        self.color = "B"
        self.create()

    def create(self):
        letters = list(ascii_lowercase)[0:8]
        for letter in letters:
            self.board[letter] = []
            for number in range(1, 9):
                self.board[letter].append(self.color)

                if number != 8:
                    if self.color == "B":
                        self.color = "W"
                    else:
                        self.color = "B"

    def get_letter_index(self, letter: str):
        return list(self.board.keys()).index(letter)

    def is_field_valid(self, field: str):
        try:
            # noinspection PyStatementEffect
            self.board[field[0]][int(field[1:]) - 1]
            return True
        except (KeyError, IndexError):
            return False


board = Board()
