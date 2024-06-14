from data.pieces.Knight import Knight


def test_knight_available_moves():
    knight = Knight("h8")
    answer = ["f7", "g6", "g1"]

    assert knight.available_moves_list == answer


def test_validate_move():
    knight = Knight("c3")

    assert knight.validate_move("a2") is True
    assert knight.validate_move("b4") is False
    assert knight.validate_move("h8") is False
    assert knight.validate_move("e2") is True
