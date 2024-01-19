import fractions
import pytest

from src.duration import meter_to_fraction, duration_to_fraction, durations_to_fractions

def test_meter_to_fraction():
    # Test case 1: meter with num = 1 and den = 2
    meter = {'type': 'meter', 'value': [{'num': 1, 'den': 2}]}
    expected_output = fractions.Fraction(1, 2)
    assert meter_to_fraction(meter) == expected_output

    # Test case 2: meter with num = 3 and den = 4
    meter = {'type': 'meter', 'value': [{'num': 3, 'den': 4}]}
    expected_output = fractions.Fraction(3, 4)
    assert meter_to_fraction(meter) == expected_output

    # Test case 3: meter with num = 5 and den = 1
    meter = {'type': 'meter', 'value': [{'num': 5, 'den': 1}]}
    expected_output = fractions.Fraction(5, 1)
    assert meter_to_fraction(meter) == expected_output

    # Test case 4: meter with num = 0 and den = 1
    meter = {'type': 'meter', 'value': [{'num': 0, 'den': 1}]}
    expected_output = fractions.Fraction(0, 1)
    assert meter_to_fraction(meter) == expected_output

    # Test case 5: meter with num = -2 and den = 3
    meter = {'type': 'meter', 'value': [{'num': -2, 'den': 3}]}
    expected_output = fractions.Fraction(-2, 3)
    assert meter_to_fraction(meter) == expected_output


def test_duration_to_fraction():
    """
    1. duration in switch, no triplet 2
    2. duration in switch, no triplet 0.062255859375
    3. duration not in switch, no triplet
    4. Achtelduole
    5. Vierteltriole
    6. Brevisquintole mit meter = 6/8
    7. Achtelseptole mit meter = 3/4
    8. punktierte halbe triole
    9. gepunktete Sechzehntel Oktole
    10. dreifach gepunktete 64tel Nontole: Fraction(5, 768)
    11. Achtelseptole mit meter == None: Exception
    12. triplet_divisor = 10: Exception
    14. triplet_divisor = 1: Exception
    """
    # Test case 1: duration in switch, no triplet, brevis
    duration = 2
    expected_output = fractions.Fraction(2, 1)
    assert duration_to_fraction(duration) == expected_output

    # Test case 2: duration in switch, no triplet, 32tel mit sieben Punkten
    duration = 0.062255859375
    expected_output = fractions.Fraction(255, 4096)
    assert duration_to_fraction(duration) == expected_output

    # Test case 3: duration not in switch, no triplet
    duration = 1.1
    with pytest.raises(Exception) as e:
        duration_to_fraction(duration)
    assert str(e.value)[0:38] == "Could not find specified note length: "

    # Test case 4: Achtelduole
    duration = 0.125
    is_triplet = True
    triplet_divisor = 2
    expected_output = fractions.Fraction(3, 16)
    assert duration_to_fraction(duration, is_triplet, triplet_divisor) == expected_output

    # Test case 5: Vierteltriole
    duration = 0.25
    is_triplet = True
    triplet_divisor = 3
    expected_output = fractions.Fraction(1, 6)
    assert duration_to_fraction(duration, is_triplet, triplet_divisor) == expected_output

    # Test case 6: Brevisquintole mit meter = 6/8
    duration = 2
    is_triplet = True
    triplet_divisor = 5
    is_compound = True
    expected_output = fractions.Fraction(6, 5)
    assert duration_to_fraction(duration, is_triplet, triplet_divisor, is_compound) == expected_output

    # Test case 7: Achtelseptole mit meter = 3/4
    duration = 0.125
    is_triplet = True
    triplet_divisor = 7
    is_compound = False
    expected_output = fractions.Fraction(1, 28)
    assert duration_to_fraction(duration, is_triplet, triplet_divisor, is_compound) == expected_output

    # Test case 8: punktierte halbe triole
    duration = 0.75
    is_triplet = True
    triplet_divisor = 3
    expected_output = fractions.Fraction(1, 2)
    assert duration_to_fraction(duration, is_triplet, triplet_divisor) == expected_output

    # Test case 9: gepunktete Sechzehntel Oktole
    duration = 0.09375
    is_triplet = True
    triplet_divisor = 8
    expected_output = fractions.Fraction(9, 256)
    assert duration_to_fraction(duration, is_triplet, triplet_divisor) == expected_output

    # Test case 10: dreifach gepunktete 64tel Nontole
    duration = 0.029296875
    is_triplet = True
    triplet_divisor = 9
    is_compound = False
    expected_output = fractions.Fraction(5, 768)
    assert duration_to_fraction(duration, is_triplet, triplet_divisor, is_compound) == expected_output

    # Test case 11: Achtelseptole mit meter == None
    duration = 0.125
    is_triplet = True
    triplet_divisor = 7
    with pytest.raises(Exception) as e:
        duration_to_fraction(duration, is_triplet, triplet_divisor)
    assert str(e.value) == "Triplet divisor 7 is not allowed without meter."

    # Test case 12: triplet_divisor = 10
    duration = 0.125
    is_triplet = True
    triplet_divisor = 10
    with pytest.raises(Exception) as e:
        duration_to_fraction(duration, is_triplet, triplet_divisor)
    assert str(e.value) == "Triplet divisor must be in range 2-9. Got 10."

    # Test case 13: triplet_divisor = 1
    duration = 0.125
    is_triplet = True
    triplet_divisor = 1
    with pytest.raises(Exception) as e:
        duration_to_fraction(duration, is_triplet, triplet_divisor)
    assert str(e.value) == "Triplet divisor must be in range 2-9. Got 1."


def test_durations_to_fractions():
    # Test case 1: voice with single note event, no triplet, not compound
    voice = [{'el_type': 'note', 'duration': 0.5}]
    expected_output = [{'el_type': 'note', 'duration': fractions.Fraction(1, 2)}]
    assert durations_to_fractions(voice) == expected_output

    # Test case 2: voice with single note event, triplet, not compound
    voice = [{'el_type': 'note', 'duration': 0.5, 'startTriplet': 3}]
    expected_output = [{'el_type': 'note', 'duration': fractions.Fraction(1, 3), 'startTriplet': 3}]
    assert durations_to_fractions(voice) == expected_output

    # Test case 3: voice with multiple note events, triplet, compound
    voice = [{'el_type': 'note', 'duration': 0.25, 'startTriplet': 3},
             {'el_type': 'note', 'duration': 0.25},
             {'el_type': 'bar', 'type': 'bar_thin_thick'},
             {'el_type': 'note', 'duration': 0.25, 'endTriplet': True}]
    expected_output = [{'el_type': 'note', 'duration': fractions.Fraction(1, 6), 'startTriplet': 3},
                       {'el_type': 'note', 'duration': fractions.Fraction(1, 6)},
                       {'el_type': 'bar', 'type': 'bar_thin_thick'},
                       {'el_type': 'note', 'duration': fractions.Fraction(1, 6), 'endTriplet': True}]
    assert durations_to_fractions(voice, is_compound=True) == expected_output

    # Test case 4: voice with no note events
    voice = [{'el_type': 'bar', 'type': 'bar_thin_thick'},
             {'el_type': 'not_a_note', 'duration': 0.25}]
    expected_output = [{'el_type': 'bar', 'type': 'bar_thin_thick'},
                       {'el_type': 'not_a_note', 'duration': 0.25}]
    assert durations_to_fractions(voice) == expected_output

    # Test case 5: voice with empty list
    voice = []
    expected_output = []
    assert durations_to_fractions(voice) == expected_output

    # Test case 6: voice with note events, triole, quintole, compound, other events, rests
    voice = [{'el_type': 'note', 'duration': 0.125, 'startTriplet': 3, 'endTriplet': True},
             {'el_type': 'note', 'duration': 0.25, 'startTriplet': 5},
             {'el_type': 'note', 'duration': 0.25},
             {'el_type': 'bar', 'type': 'bar_thin_thick'},
             {'el_type': 'note', 'duration': 0.25, 'endTriplet': True},
             {'el_type': 'note', 'duration': 0.25, 'pitches': []}]
    expected_output = [{'el_type': 'note', 'duration': fractions.Fraction(1, 12), 'startTriplet': 3, 'endTriplet': True},
                       {'el_type': 'note', 'duration': fractions.Fraction(3, 20), 'startTriplet': 5},
                       {'el_type': 'note', 'duration': fractions.Fraction(3, 20)},
                       {'el_type': 'bar', 'type': 'bar_thin_thick'},
                       {'el_type': 'note', 'duration': fractions.Fraction(3, 20), 'endTriplet': True},
                       {'el_type': 'note', 'duration': fractions.Fraction(1, 4), 'pitches': []}]
    assert durations_to_fractions(voice, is_compound=True) == expected_output