from fractions import Fraction
from src.calc_harmonies import calc_harmonies
from src.representation import pacset_equal, pcset_equal

def test_calc_harmonies_pc():
    voices = [
        [
            {
                'pitches': [9, 0],
                'duration': Fraction(1, 2)
            },
            {
                'pitches': [7, 0],
                'duration': Fraction(1, 2)
            },
            {
                'pitches': [9, 0],
                'duration': Fraction(1, 1)
            }
        ],
        [
            {
                'pitches': [0],
                'duration': Fraction(1, 4)
            },
            {
                'pitches': [5],
                'duration': Fraction(1, 2)
            },
            {
                'pitches': [4],
                'duration': Fraction(1, 4)
            },
            {
                'pitches': [5],
                'duration': Fraction(1, 1)
            },
        ]
    ]
    expected = [
        {
            'pitches': [9, 0],
            'duration': Fraction(1, 4)
        },
        {
            'pitches': [9, 0, 5],
            'duration': Fraction(1, 4)
        },
        {
            'pitches': [7, 0, 5],
            'duration': Fraction(1, 4)
        },
        {
            'pitches': [7, 0, 4],
            'duration': Fraction(1, 4)
        },
        {
            'pitches': [9, 0, 5],
            'duration': Fraction(1, 1)
        },
    ]
    actual = calc_harmonies(voices)
    assert len(actual) == len(expected)
    for i in range(len(actual)):
        assert actual[i]['duration'] == expected[i]['duration']
        assert pcset_equal(actual[i]['pitches'], expected[i]['pitches'])


def test_calc_harmonies_pac():
    voices= [
        [
            {
                'pitches': [
                    {
                        'pitch': 5,
                        'acc': 'none'
                    },
                    {
                        'pitch': 0,
                        'acc': 'none'
                    }
                ],
                'duration': Fraction(1, 2)
            },
            {
                'pitches': [
                    {
                        'pitch': 4,
                        'acc': 'none'
                    },
                    {
                        'pitch': 0,
                        'acc': 'none'
                    }
                ],
                'duration': Fraction(1, 2)
            },
            {
                'pitches': [
                    {
                        'pitch': 5,
                        'acc': 'none'
                    },
                    {
                        'pitch': 0,
                        'acc': 'none'
                    }
                ],
                'duration': Fraction(1, 1)
            }
        ],
        [
            {
                'pitches': [
                    {
                        'pitch': 0,
                        'acc': 'none'
                    }
                ],
                'duration': Fraction(1, 4)
            },
            {
                'pitches': [
                    {
                        'pitch': 3,
                        'acc': 'none'
                    }
                ],
                'duration': Fraction(1, 2)
            },
            {
                'pitches': [
                    {
                        'pitch': 2,
                        'acc': 'none'
                    }
                ],
                'duration': Fraction(1, 4)
            },
            {
                'pitches': [
                    {
                        'pitch': 3,
                        'acc': 'none'
                    }
                ],
                'duration': Fraction(1, 1)
            },
        ]
    ]
    expected = [
        {
            'pitches': [
                {
                    'pitch': 5,
                    'acc': 'none'
                },
                {
                    'pitch': 0,
                    'acc': 'none'
                }
            ],
            'duration': Fraction(1, 4)
        },
        {
            'pitches': [
                {
                    'pitch': 5,
                    'acc': 'none'
                },
                {
                    'pitch': 0,
                    'acc': 'none'
                },
                {
                    'pitch': 3,
                    'acc': 'none'
                }
            ],
            'duration': Fraction(1, 4)
        },
        {
            'pitches': [
                {
                    'pitch': 4,
                    'acc': 'none'
                },
                {
                    'pitch': 0,
                    'acc': 'none'
                },
                {
                    'pitch': 3,
                    'acc': 'none'
                }
            ],
            'duration': Fraction(1, 4)
        },
        {
            'pitches': [
                {
                    'pitch': 4,
                    'acc': 'none'
                },
                {
                    'pitch': 0,
                    'acc': 'none'
                },
                {
                    'pitch': 2,
                    'acc': 'none'
                }
            ],
            'duration': Fraction(1, 4)
        },
        {
            'pitches': [
                {
                    'pitch': 5,
                    'acc': 'none'
                },
                {
                    'pitch': 0,
                    'acc': 'none'
                },
                {
                    'pitch': 3,
                    'acc': 'none'
                }
            ],
            'duration': Fraction(1, 1)
        },
    ]
    actual = calc_harmonies(voices)
    assert len(actual) == len(expected)
    for i in range(len(actual)):
        assert actual[i]['duration'] == expected[i]['duration']
        assert pacset_equal(actual[i]['pitches'], expected[i]['pitches'])