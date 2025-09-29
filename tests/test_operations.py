import math

import pytest

from src.calculator.operations import add, divide, multiply, power, sqrt, subtract


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 3) == 7


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide_ok():
    assert divide(9, 3) == 3
    assert math.isclose(divide(7, 2), 3.5)


def test_divide_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


def test_power_sqrt():
    assert power(2, 3) == 8
    assert math.isclose(power(9, 0.5), 3.0)
    assert sqrt(16) == 4
    with pytest.raises(ValueError):
        sqrt(-1)
