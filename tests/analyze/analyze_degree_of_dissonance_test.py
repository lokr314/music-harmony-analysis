from src.analyze_degree_of_dissonance_or_atonal import analyze_degree_of_dissonance_or_atonal, calc_degree_of_dissonance, is_consonant, calc_atonality_degree


def test_analyze_degree_of_dissonance_or_atonal_empty():
    assert analyze_degree_of_dissonance_or_atonal([]) == []


def test_analyze_degree_of_dissonance_or_atonal():
    """
    Test cases:
    atonal 1
    atonal 3 (mit 10 pitches)
    atonal 5

    sauterian_formula = '/'
    sauterian_formula = 'ind.'

    Single Pitch: G# in A-Moll -> 'con' (Sauterian-Event: `([False, False, False, False, True, False, False, False, False, ], []`)
    consonant interval: F,A in C-Dur -> 'con'
    consonant chord: C-Dur in C-Dur -> 'con'

    interval false consonance: E,A in C-Dur -> 'fcon'
    chord false consonance: Dm in C-Dur -> 'fcon'
    low degree of dissonance
    med(ium) degree of dissonance
    high degree of dissonance
    """
    înput = [
        (
            ([9,11,10], 1),
            [(0, 'dur')],
            ([False, False, False, False, True, False, False, True, False], [10])
        ),
        (
            ([0,1,2,3,4,5,6,7,9,11], 1),
            [(0, 'dur')],
            ([True, True, True, True, True, True, True, True, True], [1, 3, 6])
        ),
        (
            ([0,1,2,3,4,5,6,7,8,9,10,11], 1),
            [(0, 'dur')],
            ([True, True, True, True, True, True, True, True, True], [1,3,6,8,10])
        ),
        (
            ([], 1),
            [(0, 'dur')],
            '/'
        ),
        (
            ([], 1),
            [(0, 'dur'), (0, 'moll')],
            '/'
        ),
        (
            ([3,5,7], 1),
            [(0, 'dur'), (0, 'moll')],
            'ind.'
        ),
        (
            ([8], 1),
            [(9, 'moll')],
            ([False, False, False, False, True, False, False, False, False, ], []) #con
        ),
        (
            ([5,9], 1),
            [(0, 'dur')],
            ([False, False, False, False, False, False, True, True, False], []) #con
        ),
        (
            ([0,4,7], 1),
            [(0, 'dur')],
            ([True, True, True, False, False, False, False, False, False], []) #con
        ),
        (
            ([2,5], 1),
            [(0, 'dur')],
            ([False, False, False, False, False, True, True, False, False], []) #fcon
        ),
        (
            ([2,5,9], 1),
            [(0, 'dur')],
            ([False, False, False, False, False, True, True, True, False], []) #fcon
        ),
        (
            ([0,4,11], 1),
            [(0, 'dur')],
            ([True, True, False, False, True, False, False, False, False], []) #low
        ),
        (
            ([0,2,9], 1),
            [(0, 'dur')],
            ([False, False, False, False, False, True, False, True, True], []) #med
        ),
        (
            ([4,9,11], 1),
            [(0, 'dur')],
            ([False, True, False, False, True, False, False, True, False], []) #high
        )
    ]
    expected_output = [
        (
            ([9,11,10], 1),
            [(0, 'dur')],
            ([False, False, False, False, True, False, False, True, False], [10]),
            'A1'
        ),
        (
            ([0,1,2,3,4,5,6,7,9,11], 1),
            [(0, 'dur')],
            ([True, True, True, True, True, True, True, True, True], [1, 3, 6]),
            'A3'
        ),
        (
            ([0,1,2,3,4,5,6,7,8,9,10,11], 1),
            [(0, 'dur')],
            ([True, True, True, True, True, True, True, True, True], [1,3,6,8,10]),
            'A5'
        ),
        (
            ([], 1),
            [(0, 'dur')],
            '/',
            '/'
        ),
        (
            ([], 1),
            [(0, 'dur'), (0, 'moll')],
            '/',
            '/'
        ),
        (
            ([3,5,7], 1),
            [(0, 'dur'), (0, 'moll')],
            'ind.',
            'ind.'
        ),
        (
            ([8], 1),
            [(9, 'moll')],
            ([False, False, False, False, True, False, False, False, False, ], []), #con
            'con'
        ),
        (
            ([5,9], 1),
            [(0, 'dur')],
            ([False, False, False, False, False, False, True, True, False], []), #con
            'con'
        ),
        (
            ([0,4,7], 1),
            [(0, 'dur')],
            ([True, True, True, False, False, False, False, False, False], []), #con
            'con'
        ),
        (
            ([2,5], 1),
            [(0, 'dur')],
            ([False, False, False, False, False, True, True, False, False], []), #fcon
            'fcon'
        ),
        (
            ([2,5,9], 1),
            [(0, 'dur')],
            ([False, False, False, False, False, True, True, True, False], []), #fcon
            'fcon'
        ),
        (
            ([0,4,11], 1),
            [(0, 'dur')],
            ([True, True, False, False, True, False, False, False, False], []), #low
            'low'
        ),
        (
            ([0,2,9], 1),
            [(0, 'dur')],
            ([False, False, False, False, False, True, False, True, True], []), #med
            'med'
        ),
        (
            ([4,9,11], 1),
            [(0, 'dur')],
            ([False, True, False, False, True, False, False, True, False], []), #high
            'high'
        )
    ]
    assert analyze_degree_of_dissonance_or_atonal(înput) == expected_output



def test_calc_atonality_degree():
    """
    Test cases:
    [] -> 0
    [0] -> 0
    [0,2,4,5,7,9,11] -> 0 #C-Dur
    [0,2,4,5,7,9,10] -> 1
    [4,5,6] -> 1
    [0,1,2,3,4,5,6,7,8,9,10,11] -> 5
    [0,1,2,4,6,7,8,9,10,11] -> 3
    """
    assert calc_atonality_degree([]) == 0
    assert calc_atonality_degree([0]) == 0
    assert calc_atonality_degree([0,2,4,5,7,9,11]) == 0 #C-Dur
    assert calc_atonality_degree([0,2,4,5,7,9,10]) == 0 #F-Dur
    assert calc_atonality_degree([0,2,4,5,8,9,11]) == 0 #A-Moll
    assert calc_atonality_degree([0,2,4,5,8,9,10]) == 1
    assert calc_atonality_degree([4,5,6]) == 1
    assert calc_atonality_degree([0,1,2,3,4,5,6,7,8,9,10,11]) == 5
    assert calc_atonality_degree([0,1,2,4,6,7,8,9,10,11]) == 3


def test_calc_degree_of_dissonance():
    # indifference and rest
    assert calc_degree_of_dissonance('ind.', []) == 'ind.'
    assert calc_degree_of_dissonance('/', [2,4]) == '/'

    # Atonal Pitches are allowed, they are ignored by the function.
    assert calc_degree_of_dissonance(((False, False, True, False, False, False, False, False, False), [1,2,4,5,6,4,3,2]), [7]) == "con"
    assert calc_degree_of_dissonance(((True, True, False, False, False, False, False, False, False), []), [0, 4]) == "con"
    assert calc_degree_of_dissonance(((True, True, True, False, False, False, False, False, False), []), [0, 4, 7]) == "con"
    assert calc_degree_of_dissonance(((False, False, False, False, True, True, False, False, False), [1]), [2, 11]) == "con"
    assert calc_degree_of_dissonance(((False, False, False, False, False, False, True, False, False), []), [5]) == "con"
    assert calc_degree_of_dissonance(((False, False, False, False, False, False, True, True, True), []), [5, 9, 0]) == "con"

    assert calc_degree_of_dissonance(((False, True, False, False, False, False, False, True, False), []), [4,9]) == "fcon" #E,A in C-Dur
    assert calc_degree_of_dissonance(((False, False, False, False, False, True, True, True, False), []), [2,9,5]) == "fcon" #Dm in C-Dur

    assert calc_degree_of_dissonance(((False, True, False, False, True, False, False, False, False), []), [2, 4]) == "low"
    assert calc_degree_of_dissonance(((False, True, False, False, True, True, False, False, False), []), [2, 11, 4]) == "low"
    assert calc_degree_of_dissonance(((False, True, True, True, True, True, False, False, False), []), [2, 11, 4, 7]) == "low"
    assert calc_degree_of_dissonance(((True, True, True, True, True, True, False, False, False), [1,3,6,8,10]), [2, 11, 0, 4, 7]) == "low"
    assert calc_degree_of_dissonance(((False, False, True, False, False, False, True, True, False), []), [5, 9, 7]) == "low"
    assert calc_degree_of_dissonance(((False, True, True, False, False, False, True, True, False), []), [5, 9, 4, 7]) == "low"
    assert calc_degree_of_dissonance(((True, True, True, False, False, False, True, True, True), []), [5, 9, 0, 4, 7]) == "low"

    assert calc_degree_of_dissonance(((False, False, False, False, True, True, True, True, False), []), [2, 11, 5, 9]) == "med"
    assert calc_degree_of_dissonance(((False, False, False, True, True, False, True, True, False), []), [2, 11, 5, 9, 7]) == "med"
    assert calc_degree_of_dissonance(((False, False, False, False, True, True, True, True, True), []), [2, 11, 5, 9, 0]) == "med"
    assert calc_degree_of_dissonance(((False, False, False, True, True, True, True, True, True), []), [2, 11, 5, 9, 0, 7]) == "med"

    assert calc_degree_of_dissonance(((False, True, False, False, True, True, True, True, False), []), [2, 11, 5, 9, 4]) == "high"
    assert calc_degree_of_dissonance(((False, True, True, True, False, True, True, True, False), []), [2, 5, 9, 4, 7]) == "high"
    assert calc_degree_of_dissonance(((True, True, False, False, True, True, True, True, True), []), [2, 11, 5, 9, 0, 4]) == "high"
    assert calc_degree_of_dissonance(((True, True, True, True, True, True, True, True, True), []), [2, 11, 5, 9, 0, 4, 7]) == "high"
    


def test_is_consonant():
    """
    Test cases:
    [] -> False
    [0] -> True
    [0,1] -> False
    [2,4] -> False
    [4,9] -> True
    [10,1] -> True
    [0,4,7] -> True
    [0,3,7] -> True
    [0,2,7] -> False
    [0,4,7,11] -> False
    [6,10,3] -> True
    """
    assert is_consonant([]) == False
    assert is_consonant([0]) == True
    assert is_consonant([0,1]) == False
    assert is_consonant([2,4]) == False
    assert is_consonant([4,9]) == True
    assert is_consonant([10,1]) == True
    assert is_consonant([0,4,7]) == True
    assert is_consonant([0,3,7]) == True
    assert is_consonant([0,2,7]) == False
    assert is_consonant([0,4,7,11]) == False
    assert is_consonant([6,10,3]) == True