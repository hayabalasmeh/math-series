
from math_series import __version__
from math_series.series import fibonacci
from math_series.series import lucas, sum_series


def test_version():
    assert __version__ == '0.1.0'


def test_zero():
    expected = 0
    actual = fibonacci(0)
    assert expected == actual


def test_one():
    expected = 1
    actual = fibonacci(1)
    assert expected == actual


def test_two():
    expected = 1
    actual = fibonacci(2)
    assert expected == actual


def test_three():
    expected = 2
    actual = fibonacci(3)
    assert expected == actual


# def test_fibonacci():
    # expected = []


def test_zero():
    expected = 2
    actual = lucas(0)
    assert expected == actual


def test_one():
    expected = 1
    actual = lucas(1)
    assert expected == actual


def test_two():
    expected = 3
    actual = lucas(2)
    assert expected == actual


def test_three():
    expected = 4
    actual = lucas(3)
    assert expected == actual


def test_series_fibonaci():
    expected = [0, 1, 1]
    actual = sum_series(3)
    assert expected == actual


def test_series_lucas():
    expected = [2, 1, 3, 4]
    actual = sum_series(4, 2, 1)
    assert expected == actual


def test_series_other():
    expected = [2, 3]
    actual = sum_series(5, 3)
    assert expected == actual


"""output fibonaci
0 ---0
1 --1
2---1
3 -- 2
4-- 3
5--5

"""
"""output lucas
0 --2
1--1
2--3
3--4
"""
"""
output sum_series
[first =0, second=1] and n=2 --- [0,1,1]
[first =2, second =1] and n=2 --- [2,1,3]
"""
