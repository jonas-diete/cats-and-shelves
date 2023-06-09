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

def test_start_and_finish_two_apart_returns_two1():
    assert cats_and_shelves(1, 3) == 2

def test_start_and_finish_two_apart_returns_two1():
    assert cats_and_shelves(5, 7) == 2

def test_start_and_finish_two_apart_returns_two1():
    assert cats_and_shelves(24, 26) == 2

def test_start_and_finish_three_apart_returns_one2():
    assert cats_and_shelves(1, 4) == 1

def test_start_and_finish_three_apart_returns_one1():
    assert cats_and_shelves(5, 8) == 1

def test_start_and_finish_three_apart_returns_one1():
    assert cats_and_shelves(24, 27) == 1

def test_start_and_finish_four_apart_returns_two():
    assert cats_and_shelves(1, 5) == 2

def test_start_and_finish_five_apart_returns_three():
    assert cats_and_shelves(1, 6) == 3

def test_start_and_finish_six_apart_returns_two():
    assert cats_and_shelves(1, 7) == 2

def test_start_and_finish_seven_apart_returns_three():
    assert cats_and_shelves(1, 8) == 3

def test_start_and_finish_eight_apart_returns_four():
    assert cats_and_shelves(1, 9) == 4

def test_start_and_finish_nine_apart_returns_three():
    assert cats_and_shelves(1, 10) == 3

def test_start_and_finish_ten_apart_returns_four():
    assert cats_and_shelves(1, 11) == 4