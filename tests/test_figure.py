from data.pieces.Figure import Figure


def test_get_position():
    figure = Figure("c8")
    answer = figure.get_position()

    assert answer["letters"] == ["a", "b", "c", "d", "e", "f", "g", "h"]
    assert answer["letter"] == "c"
    assert answer["number"] == 8
    assert answer["neighbours_rows"] == ["c", "b", "d"]
    assert answer["letter_index"] == 2


def test_list_available_moves():
    figure = Figure("a8")

    assert figure.list_available_moves() == []


def test_validate_move():
    figure = Figure("f7")

    assert figure.validate_move("f9") is False
