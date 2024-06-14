from data.pieces.Bishop import Bishop


def test_bishop_available_moves():
    bishop = Bishop("e7")
    answer = ["a3", "b4", "c5", "d6", "d8", "f6", "f8", "g5", "h4"]

    assert bishop.available_moves_list == answer


def test_validate_move():
    bishop = Bishop("e7")

    assert bishop.validate_move("f8") is True
    assert bishop.validate_move("g7") is False
