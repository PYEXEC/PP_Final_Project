from data.pieces.Pawn import Pawn


def test_pawn_available_moves():
    pawn = Pawn("d2")
    answer = ["d3", "d4"]

    assert pawn.available_moves_list == answer


def test_validate_move():
    pawn = Pawn("a3")

    assert pawn.validate_move("a4") is True
    assert pawn.validate_move("a1") is False
    assert pawn.validate_move("a5") is False
    assert pawn.validate_move("a2") is False
