from fractions import Fraction
import pytest

from src.to_abc_strings import analysis_to_abc_strings, sauterian_formula_to_abc_string, to_abc_strings_preprocess


def test_to_abc_strings_preprocess():
    analysis = [
        (
            ([0, 3, 4], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            'T15D15S3',
            'high'
        ),
        (
            ([0, 2, 6], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            '/',
            '/'
        ),
        (
            ([0, 1, 4], Fraction(5, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            'ind.',
            'ind.'
        ),
    ]
    harmony_lines = [
        [
            {'pitches': [0, 3, 4], 'duration': Fraction(1, 4)},
            {'pitches': [0, 2, 6], 'duration': Fraction(1, 4)},
        ],
        [
        ],
        [
            {'pitches': [0, 1, 4], 'duration': Fraction(5, 4)},
        ],
        [
        ]
    ]
    expected_output = [
        [
            (
                {'pitches': [0, 3, 4], 'duration': Fraction(1, 4)},
                [(0, 'dur'), (1, 'dur'), (2, 'moll')],
                'T15D15S3',
                'high'
            ),
            (
                {'pitches': [0, 2, 6], 'duration': Fraction(1, 4)},
                [(0, 'dur'), (1, 'dur'), (2, 'moll')],
                '/',
                '/'
            )
        ],
        [],
        [
            (
                {'pitches': [0, 1, 4], 'duration': Fraction(5, 4)},
                [(0, 'dur'), (1, 'dur'), (2, 'moll')],
                'ind.',
                'ind.'
            )
        ],
        []
    ]
    assert to_abc_strings_preprocess(analysis, harmony_lines) == expected_output


def test_analysis_to_abc_strings_pc_mode():
    analysis = [
        (
            ([0, 3, 4], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            'T15D15S3',
            'high'
        ),
        (
            ([0, 2, 6], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            '/',
            '/'
        ),
        (
            ([0, 1, 4], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            'ind.',
            'ind.'
        ),
        (
            ([0, 10, 11], Fraction(1, 4)),
            [(0, 'dur'), (10, 'dur'), (2, 'moll')],
            'T15S3A0,11,4',
            'A3'
        )
    ]
    harmony_lines = [
        [
            {'pitches': [0, 3, 4], 'duration': Fraction(1, 4)},
            {'pitches': [0, 2, 6], 'duration': Fraction(1, 4)},
        ],
        [
            {'pitches': [0, 1, 4], 'duration': Fraction(1, 4)},
            {'pitches': [0, 10, 11], 'duration': Fraction(1, 4)},
        ]
    ]
    expected_output = {
        "header": "\nL:1\nK:none\n",
        "events": [
            "[V: Analysis name=Analysis snm=A.] [C_EE]1/4 [CD^F]1/4\n",
            "[V: Analysis] [C^CE]1/4 [C_BB]1/4\n"
        ],
        "harmonic_states": [
            "w: [C,Cis,Dm]~ _\n",
            "w: [C,Cis,Dm]~ [C,Bb,Dm]\n"
        ],
        "sauterian_formula": [
            "w: T15D15S3~ /\n",
            "w: ind.~ T15S3A0,11,4\n"
        ],
        "degree_of_dissonance_or_atonal": [
            "w: high~ /\n",
            "w: ind.~ A3\n"
        ]
    }
    
    
    assert analysis_to_abc_strings(analysis, harmony_lines, mode='pc') == expected_output


def test_analysis_to_abc_strings_pac_mode():
    # also tests accidentals, Bb, B, different durations
    analysis = [
        (
            ([2,7], Fraction(511/16384)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            'T15D15S3',
            'high'
        ),
        (
            ([0,4,11], Fraction(3, 1)),
            [(0, 'dur'), (1, 'dur'), (10, 'dur')],
            '/',
            '/'
        ),
        (
            ([0,4,10], Fraction(1, 4)),
            [(0, 'dur'), (1, 'dur'), (11, 'moll')],
            'ind.',
            'ind.'
        ),
        (
            ([0,4,9], Fraction(1, 64)),
            [(0, 'dur'), (1, 'dur'), (10, 'moll')],
            'T15S3A0,11,4',
            'A3'
        )
    ]
    harmony_lines = [
        [
            {'pitches': [
                {'pitch': 0, 'acc': 'dblsharp'},
                {'pitch': 1, 'acc': 'none'},
                {'pitch': 4, 'acc': 'none'}
            ], 'duration': Fraction(511/16384)},
            {'pitches': [
                {'pitch': 0, 'acc': 'none'},
                {'pitch': 2, 'acc': 'none'},
                {'pitch': 6, 'acc': 'none'}
            ], 'duration': Fraction(3, 1)},
        ],
        [
            {'pitches': [
                {'pitch': 0, 'acc': 'none'},
                {'pitch': 2, 'acc': 'none'},
                {'pitch': 6, 'acc': 'flat'}
            ], 'duration': Fraction(1, 4)},
            {'pitches': [
                {'pitch': 0, 'acc': 'none'},
                {'pitch': 2, 'acc': 'none'},
                {'pitch': 5, 'acc': 'sharp'}
            ], 'duration': Fraction(1, 64)},
        ]
    ]
    expected_output = {
        "header": "\nL:1\nK:none\n",
        "events": [
            "[V: Analysis name=Analysis snm=A.] [^^CDG]511/16384 [CEB]3/1\n",
            "[V: Analysis] [CE_B]1/4 [CE^A]1/64\n"
        ],
        "harmonic_states": [
            "w: [C,Cis,Dm]~ [C,Cis,Bb]\n",
            "w: [C,Cis,Bm]~ [C,Cis,Bbm]\n"
        ],
        "sauterian_formula": [
            "w: T15D15S3~ /\n",
            "w: ind.~ T15S3A0,11,4\n"
        ],
        "degree_of_dissonance_or_atonal": [
            "w: high~ /\n",
            "w: ind.~ A3\n"
        ]
    }
    assert analysis_to_abc_strings(analysis, harmony_lines) == expected_output


def test_analysis_to_abc_strings_line_lengths_do_not_match():
    analysis = [
       (
            ([2,7], Fraction(511/16384)),
            [(0, 'dur'), (1, 'dur'), (2, 'moll')],
            'T15D15S3',
            'high'
        ),
        (
            ([0,4,11], Fraction(3, 1)),
            [(0, 'dur'), (1, 'dur'), (10, 'dur')],
            '/',
            '/'
        )
    ]
    harmony_lines = [
        [
            {'pitches': [
                {'pitch': 0, 'acc': 'dblsharp'},
                {'pitch': 2, 'acc': 'none'},
                {'pitch': 4, 'acc': 'none'}
            ], 'duration': Fraction(510/16384)}
        ],
        [
            {'pitches': [
                {'pitch': 0, 'acc': 'none'},
                {'pitch': 2, 'acc': 'none'},
                {'pitch': 6, 'acc': 'flat'}
            ], 'duration': Fraction(1, 4)}
        ]
    ]
    with pytest.raises(Exception) as e:
        analysis_to_abc_strings(analysis, harmony_lines)
    assert str(e.value) == "Analysis event lengths don't match line lengths."


def test_sauterian_formula_to_abc_string():
    # rest
    assert sauterian_formula_to_abc_string('/') == '/'
    # indifference
    assert sauterian_formula_to_abc_string('ind.') == 'ind.'
    # tonal
    assert sauterian_formula_to_abc_string(([True, False, True, True, False, True, False, True, False], [])) == 'T15D15S3'
    # atonal
    assert sauterian_formula_to_abc_string(([True, False, True, False, False, False, False, False, False], [0, 2, 4])) == 'T15A0,2,4'