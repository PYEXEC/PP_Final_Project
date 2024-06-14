from data.board.Board import Board


def test_create_board():
    board = Board()

    valid_board = {
        "a": ["B", "W", "B", "W", "B", "W", "B", "W"],
        "b": ["W", "B", "W", "B", "W", "B", "W", "B"],
        "c": ["B", "W", "B", "W", "B", "W", "B", "W"],
        "d": ["W", "B", "W", "B", "W", "B", "W", "B"],
        "e": ["B", "W", "B", "W", "B", "W", "B", "W"],
        "f": ["W", "B", "W", "B", "W", "B", "W", "B"],
        "g": ["B", "W", "B", "W", "B", "W", "B", "W"],
        "h": ["W", "B", "W", "B", "W", "B", "W", "B"],
    }

    assert board.board == valid_board


def test_get_letter_index():
    board = Board()

    assert board.get_letter_index("f") == 5
    assert board.get_letter_index("a") == 0


def test_is_field_valid():
    board = Board()

    assert board.is_field_valid("a5") is True
    assert board.is_field_valid("h8") is True
    assert board.is_field_valid("a10") is False
    assert board.is_field_valid("l1") is False
