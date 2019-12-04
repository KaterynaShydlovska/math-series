from series import fibonacci, lucas, sum_series

#  “Happy Path”


def test_one():
    expected = 1
    actual = fibonacci(3)
    assert actual == expected


def test_two():
    expected = 13
    actual = fibonacci(8)
    assert actual == expected


def test_three():
    expected = 1
    actual = lucas(1)
    assert actual == expected


def test_four():
    expected = 29
    actual = lucas(7)
    assert actual == expected


def test_five():
    expected = 1
    actual = sum_series(1)
    assert actual == expected


def test_six():
    expected = 1
    actual = sum_series(1, 2, 3)
    assert actual == expected
# Edge Case
#  “Happy Path”
# Expected failure


