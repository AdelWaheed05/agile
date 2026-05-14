from math_utils import add, subtract

def test_add():
    # Fixed the typo "add 1(2,3)" to "add(2,3)"
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
