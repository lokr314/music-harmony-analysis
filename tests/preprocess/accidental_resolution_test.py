from src.preprocess import accidental_resolution

def test_accidental_resolution_no_voices():
    voices = []
    accidentals = []
    barlines_with_time = []
    expected_output = []
    assert accidental_resolution(voices, accidentals, barlines_with_time) == expected_output

def test_accidental_resolution_only_empty_voices():
    voices = [
        [],
        [],
        []
    ]
    accidentals = []
    barlines_with_time = []
    expected_output = [
        [],
        [],
        []
    ]
    assert accidental_resolution(voices, accidentals, barlines_with_time) == expected_output

    # Weitere Test befinden sich in preprocess_test.py:
    # test_preprocess_accidental_resolution()
    # test_preprocess_accidental_resolution_with_chords()
    # (test_preprocess_multiple_lines()) Test ist für andere Funktionen bestimmt, nicht hierfür, benutzt aber auch accidental_resolution