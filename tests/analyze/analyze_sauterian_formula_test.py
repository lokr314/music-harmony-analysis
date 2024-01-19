from fractions import Fraction

from src.analyze_sauterian_formula import sauterian_formula, analyze_sauterian_formula

def test_sauterian_formula_tonal_result():
    """
    Test cases:
    | S13 | D35 | T1 | T3 | T5 | expected result |
    | ---- | ---- | ---- | ---- | ---- | ---- |
    | 0 | 0 | 0 | 0 | 0 | "/" |
    | 0 | 0 | 0 | 0 | 1 | T5 |
    | 0 | 0 | 0 | 1 | 0 | T3 |
    | 0 | 0 | 0 | 1 | 1 | T35 |
    | 0 | 0 | 1 | 0 | 0 | T1 |
    | 0 | 0 | 1 | 0 | 1 | T15 |
    | 0 | 0 | 1 | 1 | 0 | T13 |
    | 0 | 0 | 1 | 1 | 1 | T135 |

    | 0 | 1 | 0 | 0 | 0 | D35 |
    | 0 | 1 | 0 | 0 | 1 | D135 |
    | 0 | 1 | 0 | 1 | 0 | T3D35 |
    | 0 | 1 | 0 | 1 | 1 | T35D135 |
    | 0 | 1 | 1 | 0 | 0 | T1D35 |
    | 0 | 1 | 1 | 0 | 1 | T15D135 |
    | 0 | 1 | 1 | 1 | 0 | T13D35 |
    | 0 | 1 | 1 | 1 | 1 | T135D135 |

    | 1 | 0 | 0 | 0 | 0 | S13 |
    | 1 | 0 | 0 | 0 | 1 | T5S13 |
    | 1 | 0 | 0 | 1 | 0 | T3S13 |
    | 1 | 0 | 0 | 1 | 1 | T35S13 |
    | 1 | 0 | 1 | 0 | 0 | S135 |
    | 1 | 0 | 1 | 0 | 1 | T15S135 |
    | 1 | 0 | 1 | 1 | 0 | T13S135 |
    | 1 | 0 | 1 | 1 | 1 | T135S135 |

    | 1 | 1 | 0 | 0 | 0 | D35S13 |
    | 1 | 1 | 0 | 0 | 1 | D135S13 |
    | 1 | 1 | 0 | 1 | 0 | T3D35S13 |
    | 1 | 1 | 0 | 1 | 1 | T35D135S13 |
    | 1 | 1 | 1 | 0 | 0 | D35S135 |
    | 1 | 1 | 1 | 0 | 1 | D135S135 |
    | 1 | 1 | 1 | 1 | 0 | T13D35S135 |
    | 1 | 1 | 1 | 1 | 1 | T135D135S135 |

    For C-major: (T1, T3, T5, D1, D3, D5, S1, S3, S5) = (C, E, G, G, B, D, F, A, C) = (0, 4, 7, 7, 11, 2, 5, 9, 0)

    For F#-minor: (T1, T3, T5, D1, D3, D5, S1, S3, S5) = (Fis, A, Cis, Cis, Eis, Gis, H, D, Fis) = (6, 9, 1, 1, 5, 8, 11, 2, 6)
    """
    # rest is tested
    assert sauterian_formula((([], 1), [(0, 'dur')])) == "/"
    assert sauterian_formula((([7], 1), [(0, 'dur')])) == ([False, False, True, False, False, False, False, False, False], [])
    assert sauterian_formula((([4], 1), [(0, 'dur')])) == ([False, True, False, False, False, False, False, False, False], [])
    assert sauterian_formula((([4, 7], 1), [(0, 'dur')])) == ([False, True, True, False, False, False, False, False, False], [])
    assert sauterian_formula((([0], 1), [(0, 'dur')])) == ([True, False, False, False, False, False, False, False, False], [])
    assert sauterian_formula((([0, 7], 1), [(0, 'dur')])) == ([True, False, True, False, False, False, False, False, False], [])
    assert sauterian_formula((([0, 4], 1), [(0, 'dur')])) == ([True, True, False, False, False, False, False, False, False], [])
    assert sauterian_formula((([0, 4, 7], 1), [(0, 'dur')])) == ([True, True, True, False, False, False, False, False, False], [])

    assert sauterian_formula((([2, 11], 1), [(0, 'dur')])) == ([False, False, False, False, True, True, False, False, False], [])
    assert sauterian_formula((([2, 11, 7], 1), [(0, 'dur')])) == ([False, False, False, True, True, True, False, False, False], [])
    assert sauterian_formula((([2, 11, 4], 1), [(0, 'dur')])) == ([False, True, False, False, True, True, False, False, False], [])
    assert sauterian_formula((([2, 11, 4, 7], 1), [(0, 'dur')])) == ([False, True, True, True, True, True, False, False, False], [])
    assert sauterian_formula((([2, 11, 0], 1), [(0, 'dur')])) == ([True, False, False, False, True, True, False, False, False], [])
    assert sauterian_formula((([2, 11, 0, 7], 1), [(0, 'dur')])) == ([True, False, True, True, True, True, False, False, False], [])
    assert sauterian_formula((([2, 11, 0, 4], 1), [(0, 'dur')])) == ([True, True, False, False, True, True, False, False, False], [])
    assert sauterian_formula((([2, 11, 0, 4, 7], 1), [(0, 'dur')])) == ([True, True, True, True, True, True, False, False, False], [])

    assert sauterian_formula((([5, 9], 1), [(0, 'dur')])) == ([False, False, False, False, False, False, True, True, False], [])
    assert sauterian_formula((([5, 9, 7], 1), [(0, 'dur')])) == ([False, False, True, False, False, False, True, True, False], [])
    assert sauterian_formula((([5, 9, 4], 1), [(0, 'dur')])) == ([False, True, False, False, False, False, True, True, False], [])
    assert sauterian_formula((([5, 9, 4, 7], 1), [(0, 'dur')])) == ([False, True, True, False, False, False, True, True, False], [])
    assert sauterian_formula((([5, 9, 0], 1), [(0, 'dur')])) == ([False, False, False, False, False, False, True, True, True], [])
    assert sauterian_formula((([5, 9, 0, 7], 1), [(0, 'dur')])) == ([True, False, True, False, False, False, True, True, True], [])
    assert sauterian_formula((([5, 9, 0, 4], 1), [(0, 'dur')])) == ([True, True, False, False, False, False, True, True, True], [])
    assert sauterian_formula((([5, 9, 0, 4, 7], 1), [(0, 'dur')])) == ([True, True, True, False, False, False, True, True, True], [])

    assert sauterian_formula((([2, 11, 5, 9], 1), [(0, 'dur')])) == ([False, False, False, False, True, True, True, True, False], [])
    assert sauterian_formula((([2, 11, 5, 9, 7], 1), [(0, 'dur')])) == ([False, False, False, True, True, True, True, True, False], [])
    assert sauterian_formula((([2, 11, 5, 9, 4], 1), [(0, 'dur')])) == ([False, True, False, False, True, True, True, True, False], [])
    assert sauterian_formula((([2, 11, 5, 9, 4, 7], 1), [(0, 'dur')])) == ([False, True, True, True, True, True, True, True, False], [])
    assert sauterian_formula((([2, 11, 5, 9, 0], 1), [(0, 'dur')])) == ([False, False, False, False, True, True, True, True, True], [])
    assert sauterian_formula((([2, 11, 5, 9, 0, 7], 1), [(0, 'dur')])) == ([False, False, False, True, True, True, True, True, True], [])
    assert sauterian_formula((([2, 11, 5, 9, 0, 4], 1), [(0, 'dur')])) == ([True, True, False, False, True, True, True, True, True], [])
    assert sauterian_formula((([2, 11, 5, 9, 0, 4, 7], 1), [(0, 'dur')])) == ([True, True, True, True, True, True, True, True, True], [])


    assert sauterian_formula((([], 1), [(6, 'moll')])) == "/"
    assert sauterian_formula((([1], 1), [(6, 'moll')])) == ([False, False, True, False, False, False, False, False, False], [])
    assert sauterian_formula((([9], 1), [(6, 'moll')])) == ([False, True, False, False, False, False, False, False, False], [])
    assert sauterian_formula((([9, 1], 1), [(6, 'moll')])) == ([False, True, True, False, False, False, False, False, False], [])
    assert sauterian_formula((([6], 1), [(6, 'moll')])) == ([True, False, False, False, False, False, False, False, False], [])
    assert sauterian_formula((([6, 1], 1), [(6, 'moll')])) == ([True, False, True, False, False, False, False, False, False], [])
    assert sauterian_formula((([6, 9], 1), [(6, 'moll')])) == ([True, True, False, False, False, False, False, False, False], [])
    assert sauterian_formula((([6, 9, 1], 1), [(6, 'moll')])) == ([True, True, True, False, False, False, False, False, False], [])

    assert sauterian_formula((([8, 5], 1), [(6, 'moll')])) == ([False, False, False, False, True, True, False, False, False], [])
    assert sauterian_formula((([8, 5, 1], 1), [(6, 'moll')])) == ([False, False, False, True, True, True, False, False, False], [])
    assert sauterian_formula((([8, 5, 9], 1), [(6, 'moll')])) == ([False, True, False, False, True, True, False, False, False], [])
    assert sauterian_formula((([8, 5, 9, 1], 1), [(6, 'moll')])) == ([False, True, True, True, True, True, False, False, False], [])
    assert sauterian_formula((([8, 5, 6], 1), [(6, 'moll')])) == ([True, False, False, False, True, True, False, False, False], [])
    assert sauterian_formula((([8, 5, 6, 1], 1), [(6, 'moll')])) == ([True, False, True, True, True, True, False, False, False], [])
    assert sauterian_formula((([8, 5, 6, 9], 1), [(6, 'moll')])) == ([True, True, False, False, True, True, False, False, False], [])
    assert sauterian_formula((([8, 5, 6, 9, 1], 1), [(6, 'moll')])) == ([True, True, True, True, True, True, False, False, False], [])

    assert sauterian_formula((([11, 2], 1), [(6, 'moll')])) == ([False, False, False, False, False, False, True, True, False], [])
    assert sauterian_formula((([11, 2, 1], 1), [(6, 'moll')])) == ([False, False, True, False, False, False, True, True, False], [])
    assert sauterian_formula((([11, 2, 9], 1), [(6, 'moll')])) == ([False, True, False, False, False, False, True, True, False], [])
    assert sauterian_formula((([11, 2, 9, 1], 1), [(6, 'moll')])) == ([False, True, True, False, False, False, True, True, False], [])
    assert sauterian_formula((([11, 2, 6], 1), [(6, 'moll')])) == ([False, False, False, False, False, False, True, True, True], [])
    assert sauterian_formula((([11, 2, 6, 1], 1), [(6, 'moll')])) == ([True, False, True, False, False, False, True, True, True], [])
    assert sauterian_formula((([11, 2, 6, 9], 1), [(6, 'moll')])) == ([True, True, False, False, False, False, True, True, True], [])
    assert sauterian_formula((([11, 2, 6, 9, 1], 1), [(6, 'moll')])) == ([True, True, True, False, False, False, True, True, True], [])

    assert sauterian_formula((([8, 5, 11, 2], 1), [(6, 'moll')])) == ([False, False, False, False, True, True, True, True, False], [])
    assert sauterian_formula((([8, 5, 11, 2, 1], 1), [(6, 'moll')])) == ([False, False, False, True, True, True, True, True, False], [])
    assert sauterian_formula((([8, 5, 11, 2, 9], 1), [(6, 'moll')])) == ([False, True, False, False, True, True, True, True, False], [])
    assert sauterian_formula((([8, 5, 11, 2, 9, 1], 1), [(6, 'moll')])) == ([False, True, True, True, True, True, True, True, False], [])
    assert sauterian_formula((([8, 5, 11, 2, 6], 1), [(6, 'moll')])) == ([False, False, False, False, True, True, True, True, True], [])
    assert sauterian_formula((([8, 5, 11, 2, 6, 1], 1), [(6, 'moll')])) == ([False, False, False, True, True, True, True, True, True], [])
    assert sauterian_formula((([8, 5, 11, 2, 6, 9], 1), [(6, 'moll')])) == ([True, True, False, False, True, True, True, True, True], [])
    assert sauterian_formula((([8, 5, 11, 2, 6, 9, 1], 1), [(6, 'moll')])) == ([True, True, True, True, True, True, True, True, True], [])


def test_sauterian_formula_indifference():
    # no key and rest
    assert sauterian_formula((([], 1), [])) == "/"
    # no key and no rest
    assert sauterian_formula((([1,10], 1), [])) == "ind."

    assert sauterian_formula((([], 1), [(0, 'dur'), (1, 'dur')])) == "/"
    assert sauterian_formula((([0], 1), [(0, 'dur'), (1, 'dur')])) == "ind."
    assert sauterian_formula((([0, 4, 7], 1), [(0, 'dur'), (1, 'dur')])) == "ind."
    # atonal pitch in every key still indifferent
    assert sauterian_formula((([0, 4, 7, 11], 1), [(0, 'dur'), (1, 'dur'), (2, 'dur')])) == "ind."


def test_sauterian_formula_atonal_pitches():
    #no atonal pitches
    assert sauterian_formula((([0,2,4,5,7,9,11], 1), [(0, 'dur')])) == ([True, True, True, True, True, True, True, True, True], [])
    #all atonal pitches
    assert sauterian_formula(((list(range(12)), 1), [(0, 'dur')])) == ([True, True, True, True, True, True, True, True, True], [1, 3, 6, 8, 10])
    #some atonal pitches
    assert sauterian_formula((([0, 1, 4, 7, 8], 1), [(9, 'moll')])) == ([False, True, True, True, True, False, False, False, False], [1, 7])


def test_analyze_sauterian_formula():
    input = [
        (
            ([2,4,7], Fraction(511/16384)),
            [(0, 'dur')]
        ),
        (
            ([0,4,10], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (11, 'moll')]
        ),
        (
            ([], Fraction(1, 64)),
            [(10, 'moll')]
        ),
        (
            ([0,1,2,3,4,5,6,7,8,9,10,11], Fraction(1, 64)),
            [(0, 'dur')]
        )
    ]
    expected_output = [
        (
            ([2, 4, 7], Fraction(511, 16384)),
            [(0, 'dur')],
            ([False, True, True, True, False, True, False, False, False], [])
        ),
        (
            ([0, 4, 10], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (11, 'moll')],
            'ind.'
        ),
        (
            ([], Fraction(1, 64)),
            [(10, 'moll')],
            '/'
        ),
        (
            (list(range(12)), Fraction(1, 64)),
            [(0, 'dur')],
            ([True, True, True, True, True, True, True, True, True], [1, 3, 6, 8, 10])
        )
    ]
    assert analyze_sauterian_formula(input) == expected_output