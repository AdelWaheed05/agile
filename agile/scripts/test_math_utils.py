from math_utils import add, subtract

def test_add():
    # Make sure there is no space between 'add' and '(2, 3)'
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2
