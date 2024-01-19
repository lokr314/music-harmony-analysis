from src.preprocess import get_line_end_time
from fractions import Fraction
import pytest

def test_get_line_end_time():
    # Test case 1: All voices have the same end_time
    voices = [
        [{'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}],
        [{'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}],
        [{'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}]
    ]
    expected_output = Fraction(3, 4)
    assert get_line_end_time(voices) == expected_output

    # Test case 2: All voices have the same end_time, with different durations of single events
    voices = [
        [{'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}],
        [{'duration': Fraction(3, 4)}],
        [{'duration': Fraction(1, 8)}, {'duration': Fraction(1, 8)}, {'duration': Fraction(1, 2)}]
    ]
    expected_output = Fraction(3, 4)
    assert get_line_end_time(voices) == expected_output

    # Test case 3: Different voices have different end_times
    voices = [
        [{'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}],
        [{'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}, {'duration': Fraction(1, 8)}],
        [{'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}, {'duration': Fraction(1, 4)}]
    ]
    with pytest.raises(Exception) as e:
        get_line_end_time(voices)
    assert str(e.value) == "There are different end_times in the same line!"

    # Test case 4: Empty voices list
    voices = []
    assert get_line_end_time(voices) == Fraction(0, 1)