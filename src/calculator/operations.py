"""Core arithmetic operations with simple validation."""

from typing import Union

Number = Union[int, float]


def add(a: Number, b: Number) -> Number:
    return a + b


def subtract(a: Number, b: Number) -> Number:
    return a - b


def multiply(a: Number, b: Number) -> Number:
    return a * b


def divide(a: Number, b: Number) -> Number:
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(a: Number, b: Number) -> Number:
    return a**b


def sqrt(x: Number) -> Number:
    if x < 0:
        raise ValueError("Cannot take sqrt of negative number")
    return x**0.5
