import pytest

def square(n):
    return n ** 2

def cube(n):
    return n ** 3

def fifth_power(n):
    return n ** 5

def test_square():
    assert square(2) == 4, "Test failed, Answer should be 4"
    assert square(4) == 16, "Test failed, Answer should be 16"

def test_cube():
    assert cube(3) == 27, "Test failed, Answer should be 27"
    assert cube(10) == 1000, "Test failed, Answer should be 1000"

def test_fifth_power():
    assert fifth_power(2) == 32, "Test failed, Answer should be 32"
    assert fifth_power(10) == 100000, "Test failed, Answer should be 100000"

def test_valid_input():
    with pytest.raises(TypeError):
        square("string")

