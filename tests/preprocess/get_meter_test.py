from src.preprocess import get_meter
from fractions import Fraction

def test_get_meter_no_meter():
    # Test case 1: No meter in the first staff
    line = {'staff': [{'voices': []}]}
    assert get_meter(line)[0] == None


def test_get_meter_type_not_specified():
    # Test case 2: Meter type is not specified
    line = {'staff': [{'meter': {'type': 'unspecified'}, 'value': [{'num': 3, 'den': 4}]}]}
    assert get_meter(line)[0] == None


def test_get_meter_type_specified():
    # Test case 3: Meter type is specified and meter_to_fraction returns a valid fraction
    line = {'staff': [{'meter': {'type': 'specified', 'value': [{'num': 3, 'den': 4}]}}]}
    assert get_meter(line)[0] == Fraction(3, 4)


def test_get_meter_multiple_staffs():
    # Test case 4: Multiple line and staffs, with meter in the first staff
    line = {'staff': [
        {'meter': {'type': 'specified', 'value': [{'num': 2, 'den': 4}]}},
        {'meter': {'type': 'unspecified', 'value': [{'num': 2, 'den': 4}]}}
    ]}
    assert get_meter(line)[0] == Fraction(2, 4)

    line = {'staff': [
        {'meter': {'type': 'unspecified', 'value': [{'num': 2, 'den': 4}]}},
        {'meter': {'type': 'specified', 'value': [{'num': 2, 'den': 4}]}}
    ]}
    assert get_meter(line)[0] == None

def test_is_compound():
    line = {'staff': [{'meter': {'type': 'specified', 'value': [{'num': '3', 'den': '4'}]}}]}
    assert get_meter(line)[1] == False

    line = {'staff': [{'meter': {'type': 'specified', 'value': [{'num': '2', 'den': '8'}]}}]}
    assert get_meter(line)[1] == False

    line = {'staff': [{'meter': {'type': 'specified', 'value': [{'num': '3', 'den': '8'}]}}]}
    assert get_meter(line)[1] == True

    line = {'staff': [{'meter': {'type': 'specified', 'value': [{'num': '3', 'den': '32'}]}}]}
    assert get_meter(line)[1] == True