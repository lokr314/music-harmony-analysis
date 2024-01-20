from fractions import Fraction

from src.preprocess import abcjs_to_poac_pitches, abcjs_to_poac_event_or_bar_line, abcjs_to_poac_events_with_bar_lines, voice_to_poac_with_bar_lines, get_barlines_with_time, voices_to_poac_and_bar_lines


def test_abcjs_to_poac_pitches():
    # Test case 1: Single pitch with no accidental
    pitches = [{'pitch': 0}]
    expected_output = [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}]
    assert abcjs_to_poac_pitches(pitches) == expected_output

    # Test case 2: Single pitch with accidental
    pitches = [{'pitch': 1, 'accidental': 'sharp'}]
    expected_output = [{'pitch': 1, 'octave_pitch': 1, 'acc': 'sharp'}]
    assert abcjs_to_poac_pitches(pitches) == expected_output

    # Test case 3: Single negative pitch with accidental
    pitches = [{'pitch': -1, 'accidental': 'flat'}]
    expected_output = [{'pitch': 6, 'octave_pitch': -1, 'acc': 'flat'}]
    assert abcjs_to_poac_pitches(pitches) == expected_output

    # Test case 4: Multiple pitches with different accidentals
    pitches = [{'pitch': 2, 'accidental': 'sharp'}, {'pitch': -3, 'accidental': 'flat'}, {'pitch': 7}]
    expected_output = [{'pitch': 2, 'octave_pitch': 2, 'acc': 'sharp'}, {'pitch': 4, 'octave_pitch': -3, 'acc': 'flat'}, {'pitch': 0, 'octave_pitch': 7, 'acc': 'none'}]
    assert abcjs_to_poac_pitches(pitches) == expected_output

    # Test case 5: Empty list of pitches
    pitches = []
    expected_output = []
    assert abcjs_to_poac_pitches(pitches) == expected_output


def test_abcjs_to_poac_event_or_bar_line():
    """
    Testfälle:
    - bar
    - abcjs-event: (duration schon als fraction)
    - abcjs-event: (duration als Zahl)
    - pitches: one note with accidental
    - pitches: one -5 note
    - pitches: multiple notes with different accidentals
    - rest 
    """
    # Test case 1: bar
    abcjs_event_or_bar = {'type': 'bar_thin', 'el_type': 'bar'}
    expected_output = {'type': 'bar_thin'}
    assert abcjs_to_poac_event_or_bar_line(abcjs_event_or_bar) == expected_output

    # Test case 2: abcjs-event with duration as fraction
    abcjs_event_or_bar = {'pitches': [{'pitch': 0}], 'duration': Fraction(1, 2), 'el_type': 'note'}
    expected_output = {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)}
    assert abcjs_to_poac_event_or_bar_line(abcjs_event_or_bar) == expected_output

    # Test case 3: abcjs-event with duration as number
    abcjs_event_or_bar = {'pitches': [{'pitch': 0}], 'duration': 0.5, 'el_type': 'note'}
    expected_output = {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': 0.5}
    assert abcjs_to_poac_event_or_bar_line(abcjs_event_or_bar) == expected_output

    # Test case 4: pitches: one note with accidental
    abcjs_event_or_bar = {'pitches': [{'pitch': 1, 'accidental': 'dblsharp'}], 'duration': Fraction(1, 2), 'el_type': 'note'}
    expected_output = {'pitches': [{'pitch': 1, 'octave_pitch': 1, 'acc': 'dblsharp'}], 'duration': Fraction(1, 2)}
    assert abcjs_to_poac_event_or_bar_line(abcjs_event_or_bar) == expected_output

    # Test case 5: pitches: one -5 note
    abcjs_event_or_bar = {'pitches': [{'pitch': -5}], 'duration': Fraction(1, 2), 'el_type': 'note'}
    expected_output = {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 2)}
    assert abcjs_to_poac_event_or_bar_line(abcjs_event_or_bar) == expected_output

    # Test case 6: pitches: multiple notes with different accidentals
    abcjs_event_or_bar = {'pitches': [{'pitch': 2, 'accidental': 'sharp'}, {'pitch': -3, 'accidental': 'flat'}, {'pitch': 7}], 'duration': Fraction(1, 2), 'el_type': 'note'}
    expected_output = {'pitches': [{'pitch': 2, 'octave_pitch': 2, 'acc': 'sharp'}, {'pitch': 4, 'octave_pitch': -3, 'acc': 'flat'}, {'pitch': 0, 'octave_pitch': 7, 'acc': 'none'}], 'duration': Fraction(1, 2)}
    assert abcjs_to_poac_event_or_bar_line(abcjs_event_or_bar) == expected_output

    # Test case 7: rest
    abcjs_event_or_bar = {'rest': {'type': 'rest'}, 'duration': Fraction(1, 2), 'el_type': 'note'}
    expected_output = {'pitches': [], 'duration': Fraction(1, 2)}
    assert abcjs_to_poac_event_or_bar_line(abcjs_event_or_bar) == expected_output


def test_abcjs_to_poac_events_with_bar_lines():
    voice = [
        {'type': 'bar_thin', 'el_type': 'bar'},
        {'pitches': [{'pitch': 0}], 'duration': Fraction(1, 2), 'el_type': 'note'},
        {'pitches': [{'pitch': 1, 'accidental': 'dblsharp'}], 'duration': Fraction(1, 2), 'el_type': 'note'},
        {'pitches': [{'pitch': -5}], 'duration': Fraction(1, 2), 'el_type': 'note'},
        {'type': 'bar_dbl_repeat', 'el_type': 'bar'},
        {'pitches': [{'pitch': 2, 'accidental': 'sharp'}, {'pitch': -3, 'accidental': 'flat'}, {'pitch': 7}], 'duration': Fraction(1, 2), 'el_type': 'note'},
        {'rest': {'type': 'rest'}, 'duration': Fraction(1, 2), 'el_type': 'note'}
    ]
    expected_output = [
        {'type': 'bar_thin'},
        {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
        {'pitches': [{'pitch': 1, 'octave_pitch': 1, 'acc': 'dblsharp'}], 'duration': Fraction(1, 2)},
        {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 2)},
        {'type': 'bar_dbl_repeat'},
        {'pitches': [{'pitch': 2, 'octave_pitch': 2, 'acc': 'sharp'}, {'pitch': 4, 'octave_pitch': -3, 'acc': 'flat'}, {'pitch': 0, 'octave_pitch': 7, 'acc': 'none'}], 'duration': Fraction(1, 2)},
        {'pitches': [], 'duration': Fraction(1, 2)}
    ]
    assert abcjs_to_poac_events_with_bar_lines(voice) == expected_output


def test_voice_to_poac_with_bar_lines():
    # Test case 1: voice leer
    voice = []
    meter = Fraction(4, 4)
    expected_output = []
    assert voice_to_poac_with_bar_lines(voice, meter) == expected_output

    # Test case 2: normale abc-voice
    voice = [
                {
                  "el_type": "stem",
                  "direction": "down"
                },
                {
                  "pitches": [{"pitch": 7, "name": "c", "verticalPos": 7, "highestVert": 7, "accidental": "flat"}],
                  "duration": 0.5,
                  "el_type": "note",
                  "averagepitch": 7,
                  "minpitch": 7,
                  "maxpitch": 7
                },
                {
                  "decoration": ["accent"],
                  "pitches": [{"pitch": 8, "name": "d", "verticalPos": 8, "highestVert": 8}],
                  "duration": 0.25,
                  "el_type": "note",
                  "averagepitch": 8,
                  "minpitch": 8,
                  "maxpitch": 8
                },
                {
                  "type": "bar_thin",
                  "el_type": "bar"
                },
                {
                  'rest': {'type': 'invisible'},
                  'duration': 0.25,
                  'el_type': 'note'
                }
            ]
    meter = Fraction(4, 4)
    expected_output = [
        {
            "pitches": [{"pitch": 0, "octave_pitch": 7, "acc": "flat"}],
            "duration": Fraction(1, 2)
        },
        {
            "pitches": [{"pitch": 1, "octave_pitch": 8, "acc": "none"}],
            "duration": Fraction(1, 4)
        },
        {
            "type": "bar_thin"
        },
        {
            "pitches": [],
            "duration": Fraction(1, 4)
        }
    ]
    assert voice_to_poac_with_bar_lines(voice, meter) == expected_output


def test_get_barlines_with_time():
    """
    Testfälle:
    - leere Liste
    - keine bars
    - bar at first position
    - bar at last position, after several notes
    - bar, note, bar
    - bar, notes, bar, notes, bar
    - nur bars (alle time of zero)
    - multiple voices with barlines
    - multiple voices with different barlines
    - different bar_types
    """
    # Test case 1: leere Liste
    voices = []
    expected_output = []
    assert get_barlines_with_time(voices) == expected_output

    # Test case 2: keine bars
    voices = [
        [
            {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'pitches': [{'pitch': 1, 'octave_pitch': 1, 'acc': 'dblsharp'}], 'duration': Fraction(1, 2)},
            {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 2)}
        ]
    ]
    expected_output = []
    assert get_barlines_with_time(voices) == expected_output

    # Test case 3: bar at first position
    voices = [
        [
            {'type': 'bar_thin'},
            {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'pitches': [{'pitch': 1, 'octave_pitch': 1, 'acc': 'dblsharp'}], 'duration': Fraction(1, 2)},
            {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 2)}
        ]
    ]
    expected_output = [{'type': 'bar_thin', 'time': Fraction(0, 1)}]
    assert get_barlines_with_time(voices) == expected_output

    # Test case 4: bar at last position, after several notes
    voices = [
        [
            {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'pitches': [{'pitch': 1, 'octave_pitch': 1, 'acc': 'dblsharp'}], 'duration': Fraction(3, 16)},
            {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 5)},
            {'type': 'bar_thin'}
        ]
    ]
    expected_output = [{'type': 'bar_thin', 'time': Fraction(71, 80)}]
    assert get_barlines_with_time(voices) == expected_output

    # Test case 5: bar, note, bar
    voices = [
        [
            {'type': 'bar_thin'},
            {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'type': 'bar_thin'}
        ]
    ]
    expected_output = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thin', 'time': Fraction(1, 2)}]
    assert get_barlines_with_time(voices) == expected_output

    # Test case 6: bar, notes, bar, notes, bar, different durations
    voices = [
        [
            {'type': 'bar_thin'},
            {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'pitches': [{'pitch': 1, 'octave_pitch': 1, 'acc': 'dblsharp'}], 'duration': Fraction(3, 16)},
            {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 5)},
            {'type': 'bar_thin'},
            {'pitches': [{'pitch': 3, 'octave_pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)},
            {'pitches': [{'pitch': 4, 'octave_pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 3)},
            {'pitches': [{'pitch': 5, 'octave_pitch': 4, 'acc': 'dblflat'}], 'duration': Fraction(1, 8)},
            {'type': 'bar_thin'}
        ]
    ]
    expected_output = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thin', 'time': Fraction(71, 80)}, {'type': 'bar_thin', 'time': Fraction(383, 240)}]
    assert get_barlines_with_time(voices) == expected_output

    # Test case 7: nur bars (alle time of zero)
    voices = [
        [
            {'type': 'bar_thin'},
            {'type': 'bar_thick'},
            {'type': 'bar_left_repeat'}
        ]
    ]
    expected_output = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thick', 'time': Fraction(0, 1)}, {'type': 'bar_left_repeat', 'time': Fraction(0, 1)}]
    assert get_barlines_with_time(voices) == expected_output

    # Test case 8: multiple voices with barlines
    voices = [
        [
            {'type': 'bar_thin'},
            {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'type': 'bar_thin'}
        ],
        [
            {'type': 'bar_thin'},
            {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'type': 'bar_thin'}
        ]
    ]
    expected_output = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thin', 'time': Fraction(1, 2)}]
    assert get_barlines_with_time(voices) == expected_output

    # Test case 9: multiple voices with different barlines
    voices = [
        [
            {'type': 'bar_thin'},
            {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'type': 'bar_thin'}
        ],
        [
            {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'type': 'bar_thick'}
        ]
    ]
    expected_output = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thin', 'time': Fraction(1, 2)}]
    assert get_barlines_with_time(voices) == expected_output

    # Test case 10: different bar_types
    voices = [
        [
            {'type': 'bar_thin'},
            {'pitches': [{'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'type': 'bar_thick'},
            {'pitches': [{'pitch': 2, 'octave_pitch': -5, 'acc': 'none'}], 'duration': Fraction(1, 2)},
            {'type': 'bar_dbl_repeat'}
        ]
    ]
    expected_output = [{'type': 'bar_thin', 'time': Fraction(0, 1)}, {'type': 'bar_thick', 'time': Fraction(1, 2)}, {'type': 'bar_dbl_repeat', 'time': Fraction(1, 1)}]
    assert get_barlines_with_time(voices) == expected_output


def test_voices_to_poac_and_bar_lines():
    """
	Input:
	- voices: List of voices of one staff, where each voice is a unprocessed list (a true abcjs voice) of abcjs-objects, each with a el_type-field like 'bar', 'stem', 'note'
	- is_compound: Boolean. True, wenn die Taktart ein Vielfaches von 3 an Achteln, 16teln etc. ist, sonst False.
	
	Output:
	- voices: List of voices, where each voice is a list of poac-events: {'pitches': [{'pitch': 0-6, 'octave_pitch': int, 'acc': ''}, ...], 'duration': Fraction}
	- barlines_with_time: List of objects, each with a 'type' field and a 'time' field.

	Converts each voice of abcjs-objects to a voice of poac-events. Also returns a list of the barlines of the staff with their time.
	
    Testfälle:
    - leere Liste
    - one voice, one event
    - one voice, one bar
    - rest
    - chord with accidentals
    - one voice with events, bar lines, other objects
    - one voice, quintole, not compound meter
    - one voice, quintole, compound meter
    - multiple voices (3)
    """
    # Test case 1: leere Liste
    voices = []
    is_compound = False
    expected_voices = []
    expected_barlines = []
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)

    # Test case 2: one voice, one event
    voices = [
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
			    	}
			    ]
			]
    is_compound = False
    expected_voices = [
        [
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                "duration": Fraction(1, 2)
            }
        ]
    ]
    expected_barlines = []
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)

    # Test case 2: one voice, one bar
    voices = [
                [
                	{
                		"type": "bar_thin",
                		"el_type": "bar"
                	}
                ]
            ]
    is_compound = False
    expected_voices = [[]]
    expected_barlines = [
        {
            "type": "bar_thin",
            "time": Fraction(0, 1)
        }
    ]
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)

    # Test case 3: rest
    voices = [
                [
                	{
                		"rest": {
                			"type": "invisible"
                		},
                		"duration": 0.25,
                		"el_type": "note",
                        "averagepitch": 7,
						"minpitch": 7,
						"maxpitch": 7
                	}
                ]
            ]
    is_compound = False
    expected_voices = [
        [
            {
                "pitches": [],
                "duration": Fraction(1, 4)
            }
        ]
    ]
    expected_barlines = []
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)

    # Test case 4: chord with accidentals
    voices = [
                [
                	{
                		"pitches": [
                			{
                				"pitch": 7,
                				"name": "c",
                				"verticalPos": 7,
                				"highestVert": 7
                			},
                            {
                                "accidental": "sharp",
                				"pitch": -6,
                				"name": "B",
                				"verticalPos": 7,
                				"highestVert": 7
                			}
                		],
                		"duration": 0.5,
                		"el_type": "note",
                		"averagepitch": 7,
                		"minpitch": 7,
                		"maxpitch": 7
                	}
                ]
            ]
    is_compound = False
    expected_voices = [
        [
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    },
                    {
                        "pitch": 1,
                        "octave_pitch": -6,
                        "acc": "sharp"
                    }
                ],
                "duration": Fraction(1, 2)
            }
        ]
    ]
    expected_barlines = []
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)


    # Test case 5: one voice with events, bar lines, rests, other objects
    voices = [
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
                			},
                            {
                				"pitch": -6,
                				"name": "B",
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
						"el_type": "stem",
						"direction": "up"
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
                                "printer_shift": "different",
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
                	},
                    {
						"el_type": "stem",
						"direction": "auto"
					},
                	{
                		"rest": {
                			"type": "invisible"
                		},
                		"duration": 0.25,
                		"el_type": "note"
                	},
                    {
                        "type": "bar_thin_thick",
                        "el_type": "bar"
                    }
                ]
            ]
    is_compound = False
    expected_voices = [
        [
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    },
                    {
                        "pitch": 1,
                        "octave_pitch": -6,
                        "acc": "none"
                    }
                ],
                "duration": Fraction(1, 2)
            },
            {
                "pitches": [
                    {
                        "pitch": 1,
                        "octave_pitch": 8,
                        "acc": "none"
                    }
                ],
                "duration": Fraction(1, 4)
            },
            {
                "pitches": [],
                "duration": Fraction(1, 4)
            }
        ]
    ]
    expected_barlines = [
        {
            "type": "bar_thin",
            "time": Fraction(0, 1)
        },
        {
            "type": "bar_thin",
            "time": Fraction(3, 4)
        },
        {
            "type": "bar_thin_thick",
            "time": Fraction(4, 4)
        }
    ]
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)

    # Test case 6: one voice, quintole, not compound meter
    voices = [
					[
						{
							"startTriplet": 5,
							"tripletMultiplier": 0.4,
							"tripletR": 5,
							"pitches": [
								{
									"pitch": 7,
									"name": "c",
									"verticalPos": 7,
									"highestVert": 7
								}
							],
							"duration": 0.25,
							"el_type": "note",
							"averagepitch": 7,
							"minpitch": 7,
							"maxpitch": 7
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
							"duration": 0.25,
							"el_type": "note",
							"averagepitch": 7,
							"minpitch": 7,
							"maxpitch": 7
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
							"duration": 0.25,
							"el_type": "note",
							"averagepitch": 7,
							"minpitch": 7,
							"maxpitch": 7
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
							"duration": 0.25,
							"el_type": "note",
							"averagepitch": 7,
							"minpitch": 7,
							"maxpitch": 7
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
							"duration": 0.25,
							"endTriplet": True,
							"el_type": "note",
							"averagepitch": 7,
							"minpitch": 7,
							"maxpitch": 7
						}
					]
				]
    is_compound = False
    expected_voices = [
        [
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                "duration": Fraction(1, 10)
            },
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                "duration": Fraction(1, 10)
            },
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                "duration": Fraction(1, 10)
            },
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                "duration": Fraction(1, 10)
            },
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                "duration": Fraction(1, 10)
            }
        ]
    ]
    expected_barlines = []
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)

    # Test case 7: one voice, quintole, compound meter
    voices = [
                    [
                        {
                            "startTriplet": 5,
                            "tripletMultiplier": 0.4,
                            "tripletR": 5,
                            "pitches": [
                                {
                                    "pitch": 7,
                                    "name": "c",
                                    "verticalPos": 7,
                                    "highestVert": 7
                                }
                            ],
                            "duration": 0.25,
                            "el_type": "note",
                            "averagepitch": 7,
                            "minpitch": 7,
                            "maxpitch": 7
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
                            "duration": 0.25,
                            "el_type": "note",
                            "averagepitch": 7,
                            "minpitch": 7,
                            "maxpitch": 7
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
                            "duration": 0.25,
                            "el_type": "note",
                            "averagepitch": 7,
                            "minpitch": 7,
                            "maxpitch": 7
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
                            "duration": 0.25,
                            "el_type": "note",
                            "averagepitch": 7,
                            "endTriplet": True,
                            "minpitch": 7,
                            "maxpitch": 7
                        }
                    ]
                ]
    is_compound = True
    expected_voices = [
        [
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                #"duration": Fraction(3, 20)
                "duration": Fraction(1, 10)
            },
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                #"duration": Fraction(3, 20)
                "duration": Fraction(1, 10)
            },
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                #"duration": Fraction(3, 20)
                "duration": Fraction(1, 10)
            },
            {
                "pitches": [
                    {
                        "pitch": 0,
                        "octave_pitch": 7,
                        "acc": "none"
                    }
                ],
                #"duration": Fraction(3, 20)
                "duration": Fraction(1, 10)
            }
        ]
    ]
    expected_barlines = []
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)

    # Test case 8: multiple voices (3) with triole, barlines, rests, other objects, different durations, pointed notes, accidentals, different octaves, different bar_types, quintole, compound meter, chords
    voices = [
					[
						{
							"el_type": "stem",
							"direction": "up"
						},
						{
							"type": "bar_thin",
							"el_type": "bar"
						},
						{
							"startTriplet": 5,
							"tripletMultiplier": 0.4,
							"tripletR": 2,
							"pitches": [
								{
									"pitch": 7,
									"name": "c",
									"verticalPos": 7,
									"highestVert": 13
								}
							],
							"duration": 0.25,
							"el_type": "note",
							"averagepitch": 7,
							"minpitch": 7,
							"maxpitch": 7
						},
						{
							"pitches": [
								{
									"pitch": 9,
									"name": "e",
									"verticalPos": 9,
									"highestVert": 15
								}
							],
							"duration": 0.375,
							"endTriplet": True,
							"el_type": "note",
							"averagepitch": 9,
							"minpitch": 9,
							"maxpitch": 9
						},
						{
							"el_type": "stem",
							"direction": "up"
						},
						{
							"el_type": "stem",
							"direction": "auto"
						},
						{
							"type": "bar_thin_thin",
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
						},
						{
							"type": "bar_right_repeat",
							"el_type": "bar"
						},
						{
							"el_type": "stem",
							"direction": "auto"
						}
					],
					[
						{
							"el_type": "stem",
							"direction": "down"
						},
						{
							"el_type": "stem",
							"direction": "up"
						},
						{
							"type": "bar_thin",
							"el_type": "bar"
						},
						{
							"rest": {
								"type": "whole"
							},
							"duration": 0.75,
							"el_type": "note",
							"averagepitch": 11,
							"minpitch": 11,
							"maxpitch": 11
						},
						{
							"el_type": "stem",
							"direction": "up"
						},
						{
							"el_type": "stem",
							"direction": "auto"
						},
						{
							"type": "bar_thin_thin",
							"el_type": "bar"
						},
						{
							"rest": {
								"type": "rest"
							},
							"duration": 0.25,
							"el_type": "note",
							"averagepitch": 7,
							"minpitch": 7,
							"maxpitch": 7
						},
						{
							"type": "bar_right_repeat",
							"el_type": "bar"
						},
						{
							"el_type": "stem",
							"direction": "auto"
						}
					],
					[
						{
							"el_type": "stem",
							"direction": "down"
						},
						{
							"el_type": "stem",
							"direction": "down"
						},
						{
							"type": "bar_thin",
							"el_type": "bar"
						},
						{
							"startTriplet": 3,
							"tripletMultiplier": 0.6666666666666666,
							"tripletR": 3,
							"pitches": [
								{
									"pitch": 0,
									"name": "C",
									"verticalPos": 0,
									"highestVert": 0
								}
							],
							"duration": 0.125,
							"el_type": "note",
							"startBeam": True,
							"averagepitch": 0,
							"minpitch": 0,
							"maxpitch": 0
						},
						{
							"pitches": [
								{
									"accidental": "sharp",
									"pitch": 21,
									"name": "^c''",
									"verticalPos": 21,
									"highestVert": 21
								}
							],
							"duration": 0.125,
							"el_type": "note",
							"averagepitch": 21,
							"minpitch": 21,
							"maxpitch": 21
						},
						{
							"pitches": [
								{
									"accidental": "flat",
									"pitch": -14,
									"name": "_c,,,",
									"verticalPos": -14,
									"highestVert": -14
								}
							],
							"duration": 0.125,
							"endTriplet": True,
							"el_type": "note",
							"endBeam": True,
							"averagepitch": -14,
							"minpitch": -14,
							"maxpitch": -14
						},
						{
							"type": "bar_thin_thin",
							"el_type": "bar"
						},
						{
							"duration": 0.375,
							"pitches": [
								{
									"pitch": 7,
									"name": "c",
									"verticalPos": 7,
									"highestVert": 7
								},
								{
									"pitch": 9,
									"name": "e",
									"verticalPos": 9,
									"highestVert": 9
								},
								{
									"pitch": 12,
									"name": "a",
									"verticalPos": 12,
									"printer_shift": "different",
									"highestVert": 12
								},
								{
									"pitch": 13,
									"name": "b",
									"verticalPos": 13,
									"highestVert": 13
								}
							],
							"el_type": "note",
							"averagepitch": 10.25,
							"minpitch": 7,
							"maxpitch": 13
						},
						{
							"type": "bar_right_repeat",
							"el_type": "bar"
						}
					]
				]
    is_compound = True
    expected_voices = [
        [
            {
                'pitches': [
                    {'pitch': 0, 'octave_pitch': 7, 'acc': 'none'},
                ],
                #"duration": Fraction(3, 20)
                "duration": Fraction(1, 10)
            },
            {
                'pitches': [
                    {'pitch': 2, 'octave_pitch': 9, 'acc': 'none'},
                ],
                #"duration": Fraction(9, 40)
                "duration": Fraction(3, 20)
            },
            {
                'pitches': [
                    {'pitch': 1, 'octave_pitch': 8, 'acc': 'none'},
                ],
                'duration': Fraction(1, 2)
            }
        ],
        [
            {
                'pitches': [],
                'duration': Fraction(3, 4)
            },
            {
                'pitches': [],
                'duration': Fraction(1, 4)
            }
        ],
        [
            {
                'pitches': [
                    {'pitch': 0, 'octave_pitch': 0, 'acc': 'none'}
                ],
                'duration': Fraction(1, 12)
            },
            {
                'pitches': [
                    {'pitch': 0, 'octave_pitch': 21, 'acc': 'sharp'}
                ],
                'duration': Fraction(1, 12)
            },
            {
                'pitches': [
                    {'pitch': 0, 'octave_pitch': -14, 'acc': 'flat'}
                ],
                'duration': Fraction(1, 12)
            },
            {
                'pitches': [
                    {'pitch': 0, 'octave_pitch': 7, 'acc': 'none'},
                    {'pitch': 2, 'octave_pitch': 9, 'acc': 'none'},
                    {'pitch': 5, 'octave_pitch': 12, 'acc': 'none'},
                    {'pitch': 6, 'octave_pitch': 13, 'acc': 'none'}
                ],
                'duration': Fraction(3, 8)
            }
        ]
    ]
    expected_barlines = [
        {
            'type': 'bar_thin',
            'time': Fraction(0, 1)
        },
        {
            'type': 'bar_thin_thin',
            #'time': Fraction(3, 8)
            'time': Fraction(1, 4)
        },
        {
            'type': 'bar_right_repeat',
            #'time': Fraction(7, 8)
            'time': Fraction(3, 4)
        }
    ]
    assert voices_to_poac_and_bar_lines(voices, is_compound) == (expected_voices, expected_barlines)
                