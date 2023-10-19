import pytest
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str(): # strings are test with "with" and importing "pytest" for the remaining library of testing functions
    with pytest.raises(TypeError):
        square("cat")