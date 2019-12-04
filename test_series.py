from series import fibonacci, lucas, sum_series

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

#For one argument
def test_five():
    expected = 34
    actual = sum_series(10)
    assert actual == expected


def test_six():
    expected = 3
    actual = sum_series(5)
    assert actual == expected

# For 3 arguments
def test_seven():
    expected = 15127
    actual = sum_series(20, 2, 1)
    assert actual == expected


def test_eight():
    expected = 7
    actual = sum_series(4, 2, 1)
    assert actual == expected



