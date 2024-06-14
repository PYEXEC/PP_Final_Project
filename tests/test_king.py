from data.pieces.King import King


def test_king_available_moves():
    king = King("d4")
    answer = ["d3", "d5", "c3", "c4", "c5", "e3", "e4", "e5"]

    assert king.available_moves_list == answer


def test_validate_move():
    king = King("h8")

    assert king.validate_move("h7") is True
    assert king.validate_move("a1") is False
