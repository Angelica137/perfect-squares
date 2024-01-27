from squares import squares_to_odd


def test_squares_to_odd_56():
    assert squares_to_odd(9, 5) == "9^2 - 5^2 = 11 + 13 + 15 + 17 = 56"


def test_squares_to_odd_51():
    assert squares_to_odd(10, 7) == "10^2 - 7^2 = 15 + 17 + 19 = 51"


def test_squares_to_odd_396():
    assert squares_to_odd(100, 98) == "100^2 - 98^2 = 197 + 199 = 396"


def test_squares_to_odd_199():
    assert squares_to_odd(100, 99) == "100^2 - 99^2 = 199 = 199"
