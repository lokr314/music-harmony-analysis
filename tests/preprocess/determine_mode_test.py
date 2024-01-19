from src.preprocess import determine_mode
import pytest

"""
- `lines == []`
- `lines[0]['staff]` not defined
- meter not in first_staff
- meter type not specified
- bar at first position.
- bar at the position directly after a full meter -> Should return 'bar'
- bar at a position, where a note starts in the first meter, but goes longer than the meter, than comes the bar -> Should return 'single'
- bar after first meter
"""


def test_empty_lines():
    """
    Wenn lines leer ist, soll eine Exception geworfen werden.
    """
    lines = []
    with pytest.raises(Exception) as e:
        determine_mode(lines)
    assert str(e.value) == "No lines defined."


def test_staff_not_defined():
    """
    Wenn staff nicht definiert ist, soll eine Exception geworfen werden.
    """
    lines = [
        {
            'foo': 'bar'
        }
    ]
    with pytest.raises(Exception) as e:
        determine_mode(lines)
    assert str(e.value) == "No staff defined."


def test_meter_not_in_first_staff():
    """
    Wenn meter nicht in der ersten Notenzeile definiert ist, soll der Modus 'single' sein.
    """
    lines = [
        {
            'staff': [
                {
                    'clef': 'treble',
                    'key': 'C',
                    'voices': [
                        [ 
                            {
                              "pitches": [
                                {
                                  "pitch": 7,
                                  "name": "c",
                                  "verticalPos": 7,
                                  "highestVert": 7
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            },
                            {
                              "decoration": [
                                "accent"
                              ],
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.25,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            },
                            {
                              "type": "bar_thin",
                              "el_type": "bar"
                            }
                        ],
                        [
                            {
                              "el_type": "note",
                              "duration": 0.75,
                              "rest": {
                                "type": "invisible"
                              },
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            }
                        ]               
                    ]
                }
            ]
        }
    ]
    assert determine_mode(lines) == 'single'


def test_meter_type_not_specified():
    """
    Wenn das type-Attribut von meter nicht den Wert 'specified' hat, soll der Modus 'single' sein.
    """
    lines = [
        {
            'staff': [
                {
                    'clef': 'treble',
                    'key': 'C',
                    'meter': {
                        'type': 'unspecified',
                        'value': [
                            {
                                'num': 4,
                                'den': 4
                            }
                        ]
                    },
                    'voices': [
                        [ 
                            {
                              "pitches": [
                                {
                                  "pitch": 7,
                                  "name": "c",
                                  "verticalPos": 7,
                                  "highestVert": 7
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            },
                            {
                              "decoration": [
                                "accent"
                              ],
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.25,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            },
                            {
                              "type": "bar_thin",
                              "el_type": "bar"
                            }
                        ],
                        [
                            {
                              "el_type": "note",
                              "duration": 0.75,
                              "rest": {
                                "type": "invisible"
                              },
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            }
                        ]               
                    ]
                }
            ]
        }
    ]
    assert determine_mode(lines) == 'single'


def test_bar_at_first_position():
    """
    Wenn am Anfang eine barline steht, soll der Modus 'bar' sein.
    """
    lines = [
        {
            'staff': [
                {
                    'clef': 'treble',
                    'key': 'C',
                    'meter': {
                        'type': 'specified',
                        'value': [
                            {
                                'num': 4,
                                'den': 4
                            }
                        ]
                    },
                    'voices': [
                        [ 
                            {
                              "type": "bar_thin",
                              "el_type": "bar"
                            },
                            {
                              "pitches": [
                                {
                                  "pitch": 7,
                                  "name": "c",
                                  "verticalPos": 7,
                                  "highestVert": 7
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            },
                            {
                              "decoration": [
                                "accent"
                              ],
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.25,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            }
                        ],
                        [
                            {
                              "el_type": "note",
                              "duration": 0.75,
                              "rest": {
                                "type": "invisible"
                              },
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            }
                        ]               
                    ]
                }
            ]
        }
    ]
    assert determine_mode(lines) == 'bar'


def test_bar_at_position_directly_after_full_meter():
    """
    Wenn direkt nach einem ganzen Takt eine barline steht, soll der Modus 'bar' sein.
    """
    lines = [
        {
            'staff': [
                {
                    'clef': 'treble',
                    'key': 'C',
                    'meter': {
                        'type': 'specified',
                        'value': [
                            {
                                'num': 4,
                                'den': 4
                            }
                        ]
                    },
                    'voices': [
                        [ 
                            {
                              "pitches": [
                                {
                                  "pitch": 7,
                                  "name": "c",
                                  "verticalPos": 7,
                                  "highestVert": 7
                                }
                              ],
                              "duration": 1,
                              "el_type": "note",
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            },
                            {
                              "type": "bar_thin",
                              "el_type": "bar"
                            },
                            {
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            }
                        ],
                        [
                            {
                              "el_type": "note",
                              "duration": 0.75,
                              "rest": {
                                "type": "invisible"
                              },
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            }
                        ]               
                    ]
                }
            ]
        }
    ]
    assert determine_mode(lines) == 'bar'


def test_bar_at_position_where_note_starts_in_first_meter_but_goes_longer_than_meter():
    """
    Wenn eine Note im ersten Takt beginnt, aber länger als ein Takt geht, und dann eine barline kommt, soll der Modus 'single' sein.
    """
    lines = [
        {
            'staff': [
                {
                    'clef': 'treble',
                    'key': 'C',
                    'meter': {
                        'type': 'specified',
                        'value': [
                            {
                                'num': 4,
                                'den': 4
                            }
                        ]
                    },
                    'voices': [
                        [ 
                            {
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            },
                            {
                              "pitches": [
                                {
                                  "pitch": 7,
                                  "name": "c",
                                  "verticalPos": 7,
                                  "highestVert": 7
                                }
                              ],
                              "duration": 1,
                              "el_type": "note",
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            },
                            {
                              "type": "bar_thin",
                              "el_type": "bar"
                            }
                        ],
                        [
                            {
                              "el_type": "note",
                              "duration": 0.75,
                              "rest": {
                                "type": "invisible"
                              },
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            }
                        ]               
                    ]
                }
            ]
        }
    ]
    assert determine_mode(lines) == 'single'


def test_bar_after_first_meter():
    """
    Wenn eine barline nach dem ersten Takt kommt, soll der Modus 'bar' sein.
    """
    lines = [
        {
            'staff': [
                {
                    'clef': 'treble',
                    'key': 'C',
                    'meter': {
                        'type': 'specified',
                        'value': [
                            {
                                'num': 4,
                                'den': 4
                            }
                        ]
                    },
                    'voices': [
                        [ 
                            {
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            },
                            {
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            },
                            {
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            },
                            {
                              "type": "bar_thin",
                              "el_type": "bar"
                            }
                        ],
                        [
                            {
                              "el_type": "note",
                              "duration": 0.75,
                              "rest": {
                                "type": "invisible"
                              },
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            }
                        ]
                    ]
                }
            ]
        }
    ]
    assert determine_mode(lines) == 'single'


def test_bar_in_second_voice():
    """
    Wenn eine barline in der zweiten Stimme kommt, soll der Modus 'single' sein.
    """
    lines = [
        {
            'staff': [
                {
                    'clef': 'treble',
                    'key': 'C',
                    'meter': {
                        'type': 'specified',
                        'value': [
                            {
                                'num': 4,
                                'den': 4
                            }
                        ]
                    },
                    'voices': [
                        [ 
                            {
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            },
                            {
                              "pitches": [
                                {
                                  "pitch": 8,
                                  "name": "d",
                                  "verticalPos": 8,
                                  "highestVert": 8
                                }
                              ],
                              "duration": 0.5,
                              "el_type": "note",
                              "averagepitch": 8,
                              "minpitch": 8,
                              "maxpitch": 8
                            }
                        ],
                        [
                            {
                              "type": "bar_thin",
                              "el_type": "bar"
                            },
                            {
                              "el_type": "note",
                              "duration": 0.75,
                              "rest": {
                                "type": "invisible"
                              },
                              "averagepitch": 7,
                              "minpitch": 7,
                              "maxpitch": 7
                            }
                        ]
                    ]
                }
            ]
        }
    ]
    assert determine_mode(lines) == 'single'