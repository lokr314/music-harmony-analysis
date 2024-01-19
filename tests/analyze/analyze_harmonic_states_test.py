from fractions import Fraction

from src.analyze_harmonic_states import analyze_harmonic_states


def test_analyze_harmonic_states_d7():
    input = [
        ([2, 5, 7, 11], Fraction(1, 4))
    ]
    expected_output = [
        (([2, 5, 7, 11], Fraction(1, 4)), [(0, 'dur'), (0, 'moll')])
    ]
    assert analyze_harmonic_states(input) == expected_output


def test_analyze_harmonic_states_modulation():
    input = [
        ([2, 5, 7, 11], Fraction(1, 4)), # G7
        ([0, 4, 7], Fraction(1, 4)), # C
        ([2, 6, 9], Fraction(1, 4)), # D
        ([2, 7, 11], Fraction(1, 4)) # G
    ]
    expected_output = [
        (([2, 5, 7, 11], Fraction(1, 4)), [(0, 'dur'), (0, 'moll')]),
        (([0, 4, 7], Fraction(1, 4)), [(0, 'dur')]), 
        (([2, 6, 9], Fraction(1, 4)), [(7, 'dur')]), # modulating pitch 6 ~ Fis -> modulation to G major
        (([2, 7, 11], Fraction(1, 4)), [(7, 'dur')])
    ]
    assert analyze_harmonic_states(input) == expected_output


def test_analyze_harmonic_states_indifference():
    input = [
        ([2, 5, 7, 11], Fraction(1, 4)), # G7
        ([0, 3, 7], Fraction(1, 4)), # Cm
        ([1,4,7,10], Fraction(1, 4)), # e diminshed
        ([5], Fraction(1, 4)), # pitch F
    ]
    expected_output = [
        (([2, 5, 7, 11], Fraction(1, 4)), [(0, 'dur'), (0, 'moll')]),
        (([0, 3, 7], Fraction(1, 4)), [(0, 'moll')]), 
        (([1,4,7,10], Fraction(1, 4)), [(5, 'moll'), (8, 'moll')]), # Indifference: Two possible keys Fm and Asm
        (([5], Fraction(1, 4)), [(5, 'moll')])
    ]
    assert analyze_harmonic_states(input) == expected_output


def test_analyze_harmonic_states_atonal_chord():
    input = [
        ([0, 1, 2], Fraction(1, 4)) # C, Cis, D
    ]
    expected_output = [
        (([0, 1, 2], Fraction(1, 4)), [
            (0, 'dur'),
            (0, 'moll'),
            (1, 'dur'),
            (1, 'moll'),
            (2, 'dur'),
            (2, 'moll'),
            (3, 'dur'),
            (5, 'dur'),
            (5, 'moll'),
            (6, 'moll'),
            (7, 'dur'),
            (7, 'moll'),
            (8, 'dur'),
            (9, 'dur'),
            (9, 'moll'),
            (10, 'dur'),
            (10, 'moll'),
            (11, 'moll')
        ])
    ]
    assert analyze_harmonic_states(input) == expected_output


def test_analyze_harmonic_states_tristan():
    """
    The music for tristan:

    1. [a]1/8
    2. [f]5/8
    3. [e]1/8
    4. [dis, f, gis, h]5/8
    5. [dis, f, a, h]1/8
    6. [d, e, gis, ais]1/8
    7. [d, e, gis, h]5/8

    expected harmonic states:
    1. [C, Cism, D, Dm, E, Em, F, Fism, G, Gm, A, Am, Bb, Bbm]
    2. [F,Bb,C,Fism,Am,Bbm,Dm]
    3. [F,C,Am,Dm]
    4. [Cm]
    5. [Cm]
    6. [Es]
    7. [Am]
    """
    input = [
        ([9], Fraction(1, 8)),
        ([5], Fraction(5, 8)),
        ([4], Fraction(1, 8)),
        ([3, 5, 8, 11], Fraction(5, 8)),
        ([3, 5, 9, 11], Fraction(1, 8)),
        ([2, 4, 8, 10], Fraction(1, 8)),
        ([2, 4, 8, 11], Fraction(5, 8))
    ]
    expected_output = [
        (([9], Fraction(1, 8)), [(0, 'dur'), (1, 'moll'), (2, 'dur'), (2, 'moll'), (4, 'dur'), (4, 'moll'), (5, 'dur'), (6, 'moll'), (7, 'dur'), (7, 'moll'), (9, 'dur'), (9, 'moll'), (10, 'dur'), (10, 'moll')]),
        (([5], Fraction(5, 8)), [(0, 'dur'), (2, 'moll'), (5, 'dur'), (6, 'moll'), (9, 'moll'), (10, 'dur'), (10, 'moll')]),
        (([4], Fraction(1, 8)), [(0, 'dur'), (2, 'moll'), (5, 'dur'), (9, 'moll')]),
        (([3, 5, 8, 11], Fraction(5, 8)), [(0, 'moll')]),
        (([3, 5, 9, 11], Fraction(1, 8)), [(0, 'moll')]),
        (([2, 4, 8, 10], Fraction(1, 8)), [(3, 'dur')]),
        (([2, 4, 8, 11], Fraction(5, 8)), [(9, 'moll')])
    ]
    assert analyze_harmonic_states(input) == expected_output