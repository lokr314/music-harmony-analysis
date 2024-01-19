from fractions import Fraction

from src.preprocess import remove_thin_thin_barlines_if_not_bar_line

def test_remove_thin_thin_barlines_if_not_bar_line():
    """
	Input:
	- barlines_with_time: List of objects, each with a 'type' field and a 'time' field.
	The 'type' field is either 'bar_thin', 'bar_thin_thin', 'bar_thick_thin', 'bar_thin_thick', 'bar_right_repeat', 'bar_left_repeat', 'bar_dbl_repeat'.
	The 'time' field is a Fraction.
	- meter: Fraction. Die Länge eines Taktes.
	
	Output:
	- barlines_with_time: List of objects, each with a 'type' field and a 'time' field.

	Removes barlines with type 'bar_thin_thin' if ((their time is not exactly a meter bigger than the time of the previous barline) or, if at first index: (their time is not exactly a meter bigger than 0) or (their time is not 0)).
	
    Testfälle:
    - thinthin time 0 at first index
    - thinthin time 0 at second index
    - thinthin time = meter at first index
    - thinthin time > 0, time < meter at first index
    - thinthin time > 0, time > meter at first index
    - otherbar at time 0, thinthin time < meter
    - otherbar at time 0, thinthin time = meter
    - otherbar at 0 < time < meter , thinthin.time = meter # sollte falsch sein
    - otherbar at 0 < time < meter , thinthin.time = meter + otherbar.time
    - otherbar at 0 < time < meter , thinthin.time > meter + otherbar.time # sollte falsch sein
    - otherbar at meter, thinthin < otherbar.time + meter
    - otherbar at meter, thinthin = otherbar.time + meter
    - otherbar at meter, thinthin > otherbar.time + meter
    - leere liste
    - nur otherbarlines
    - nur thinthins, meinetwegen jeden Schlag einen
    - nur thinthins, jetzt aber strikt nach meter, mit thinthin at 0
    - nur thinthins, jetzt aber strikt nach meter, ohne thinthin at 0
    - bar 0 , thinthin 3, bar 4 im 4/4
    - bar 0 , thinthin 3, bar 4 im 3/4
    """
    # Test case 1: thinthin time 0 at first index
    barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(0, 1)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(0, 1)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 2: thinthin time 0 at second index
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thin_thin', 'time': Fraction(0, 1)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 1)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 3: thinthin time = meter at first index
    barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(4, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(4, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 4: thinthin time > 0, time < meter at first index
    barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(1, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = []
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 5: thinthin time > 0, time > meter at first index
    barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(5, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = []
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 6: otherbar at time 0, thinthin time < meter
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thin_thin', 'time': Fraction(1, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 1)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 7: otherbar at time 0, thinthin time = meter
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thin_thin', 'time': Fraction(4, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thin_thin', 'time': Fraction(4, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 8: otherbar at 0 < time < meter , thinthin.time = meter
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(1, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(4, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(1, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 9: otherbar at 0 < time < meter , thinthin.time = meter + otherbar.time
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(1, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(5, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(1, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(5, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 10: otherbar at 0 < time < meter , thinthin.time > meter + otherbar.time
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(1, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(8, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(1, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 11: otherbar at meter, thinthin < otherbar.time + meter
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(5, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(4, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 12: otherbar at meter, thinthin = otherbar.time + meter
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(8, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(8, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 13: otherbar at meter, thinthin > otherbar.time + meter
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(9, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(4, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 14: leere liste
    barlines_with_time = []
    meter = Fraction(4, 4)
    expected_barlines_with_time = []
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 15: nur otherbarlines
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 4)}, {'type': 'bar_thin', 'time': Fraction(1, 4)}, {'type': 'bar_thin', 'time': Fraction(2, 4)}, {'type': 'bar_thin', 'time': Fraction(3, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 4)}, {'type': 'bar_thin', 'time': Fraction(1, 4)}, {'type': 'bar_thin', 'time': Fraction(2, 4)}, {'type': 'bar_thin', 'time': Fraction(3, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 16: nur thinthins, jeden Schlag einen
    barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(0, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(1, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(2, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(3, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(5, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(0, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(4, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 17: nur thinthins, strikt nach meter, mit thinthin at 0
    barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(0, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(8, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(12, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(0, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(8, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(12, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 18: nur thinthins, strikt nach meter, ohne thinthin at 0
    barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(8, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(12, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin_thin', 'time': Fraction(4, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(8, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(12, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 19: bar 0 , thinthin 3, bar 4 im 4/4
    barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(3, 4)}, {'type': 'bar_thin', 'time': Fraction(4, 4)}]
    meter = Fraction(4, 4)
    expected_barlines_with_time = [{'type': 'bar_thin', 'time': Fraction(0, 4)}, {'type': 'bar_thin', 'time': Fraction(4, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time

    # Test case 20: bar 0 , thinthin 3, bar 4 im 3/4
    barlines_with_time = [{'type': 'bar_thick', 'time': Fraction(0, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(3, 4)}, {'type': 'bar_thick', 'time': Fraction(4, 4)}]
    meter = Fraction(3, 4)
    expected_barlines_with_time = [{'type': 'bar_thick', 'time': Fraction(0, 4)}, {'type': 'bar_thin_thin', 'time': Fraction(3, 4)}, {'type': 'bar_thick', 'time': Fraction(4, 4)}]
    assert remove_thin_thin_barlines_if_not_bar_line(barlines_with_time, meter) == expected_barlines_with_time