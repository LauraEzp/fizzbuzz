
import pytest
from fizzbuzz import fizzbuzz

@pytest.mark.parametrize("number, expected", [
    (1, "1"),
    (3, "FizzFizz"),
    (5, "BuzzBuzz"),
    (9, "Fizz"),
    (13, "Fizz"),
    (15, "FizzBuzzBuzz"),
    (25, "BuzzBuzz"),
    (30, "FizzFizzBuzz"),
    (33, "FizzFizz"),
    (35, "FizzBuzzBuzz"),
    (51, "FizzBuzz"),
    (53, "FizzBuzz"),
    (55, "BuzzBuzz"),
    (75, "FizzBuzzBuzz"),
])
def test_fizzbuzz(number, expected):
    assert fizzbuzz(number) == expected
