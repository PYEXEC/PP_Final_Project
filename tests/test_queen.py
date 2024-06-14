from data.pieces.Queen import Queen


def test_queen_available_moves():
    queen = Queen("c2")
    answer = {
        "a2",
        "a4",
        "b1",
        "b2",
        "b3",
        "c1",
        "c3",
        "c4",
        "c5",
        "c6",
        "c7",
        "c8",
        "d1",
        "d2",
        "d3",
        "e2",
        "e4",
        "f2",
        "f5",
        "g2",
        "g6",
        "h2",
        "h7",
    }

    assert queen.available_moves_list == answer


def test_validate_move():
    queen = Queen("d7")

    assert queen.validate_move("d7") is False
    assert queen.validate_move("a4") is True
    assert queen.validate_move("d1") is True
    assert queen.validate_move("d7") is False
    assert queen.validate_move("d3") is True
