import pytest

from calculations import (
    analyze_numbers,
    calculate_average,
    count_positive,
    find_max,
)


def test_average_positive():
    assert calculate_average([10, 20, 30]) == 20


def test_average_single_value():
    assert calculate_average([5]) == 5


def test_average_negative():
    assert calculate_average([-10, 0, 10]) == 0


def test_find_max_negative():
    assert find_max([-10, -5, -20]) == -5


def test_find_max_mixed():
    assert find_max([3, 7, -1, 7]) == 7


def test_count_positive_with_zero():
    assert count_positive([-1, 0, 1]) == 1


def test_count_positive_all_negative():
    assert count_positive([-3, -2, -1]) == 0


def test_count_positive_all_positive():
    assert count_positive([1, 2, 3]) == 3


def test_average_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])


def test_find_max_empty_list():
    with pytest.raises(ValueError):
        find_max([])


def test_analyze_mixed():
    assert analyze_numbers([3, 1, 2]) == (1, 3, 2)


def test_analyze_all_negative():
    assert analyze_numbers([-5, -1, -3]) == (-5, -1, -3)


def test_analyze_all_positive():
    assert analyze_numbers([10, 20]) == (10, 20, 15)


def test_analyze_single_value():
    assert analyze_numbers([7]) == (7, 7, 7)


def test_analyze_with_zero():
    assert analyze_numbers([-2, 0, 2]) == (-2, 2, 0)


def test_analyze_empty_list():
    with pytest.raises(ValueError):
        analyze_numbers([])
