from src.preprocess import get_accidentals

def test_get_accidentals():
    # Test case 1: staff with no accidentals
    staff = {'key': {'accidentals': []}}
    expected_output = []
    assert get_accidentals(staff) == expected_output

    # Test case 2: staff with one accidental
    staff = {'key': {'accidentals': [{'acc': 'sharp', 'note': 'C'}]}}
    expected_output = [{'acc': 'sharp', 'pitch': 0}]
    assert get_accidentals(staff) == expected_output

    # Test case 3: staff with multiple accidentals
    staff = {'key': {'accidentals': [{'acc': 'sharp', 'note': 'C'}, {'acc': 'flat', 'note': 'D'}, {'acc': 'natural', 'note': 'E'}]}}
    expected_output = [{'acc': 'sharp', 'pitch': 0}, {'acc': 'flat', 'pitch': 1}, {'acc': 'natural', 'pitch': 2}]
    assert get_accidentals(staff) == expected_output

    # Test case 4: staff with no accidentals and empty key attribute
    staff = {'key': {}}
    expected_output = []
    assert get_accidentals(staff) == expected_output

    # Test case 5: staff with no key attribute
    staff = {}
    expected_output = []
    assert get_accidentals(staff) == expected_output