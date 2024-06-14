from data.pieces.Rook import Rook


def test_rook_available_moves():
    rook = Rook("a1")
    answer = [
        "a2",
        "a3",
        "a4",
        "a5",
        "a6",
        "a7",
        "a8",
        "b1",
        "c1",
        "d1",
        "e1",
        "f1",
        "g1",
        "h1",
    ]

    assert rook.available_moves_list == answer


def test_validate_move():
    rook = Rook("g4")

    assert rook.validate_move("g8") is True
    assert rook.validate_move("a10") is False
    assert rook.validate_move("g4") is False
    assert rook.validate_move("f5") is False
