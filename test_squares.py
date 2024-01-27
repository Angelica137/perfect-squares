from squares import squares_to_odd


def test_squares_to_odd_56():
    assert squares_to_odd(9, 5) == "56, [11, 13, 15, 17]"


def test_squares_to_odd_51():
    assert squares_to_odd(10, 7) == "51, [15, 17, 19]"


def test_squares_to_odd_396():
    assert squares_to_odd(100, 98) == "396, [197, 199]"
