from cats_and_shelves import cats_and_shelves

def test_start_and_finish_one_returns_zero():
    assert cats_and_shelves(1, 1) == 0

def test_start_and_finish_three_returns_zero():
    assert cats_and_shelves(3, 3) == 0

def test_start_and_finish_twentyfour_returns_zero():
    assert cats_and_shelves(24, 24) == 0

def test_start_and_finish_one_apart_returns_one1():
    assert cats_and_shelves(1, 2) == 1

def test_start_and_finish_one_apart_returns_one2():
    assert cats_and_shelves(5, 6) == 1

def test_start_and_finish_one_apart_returns_one3():
    assert cats_and_shelves(24, 25) == 1