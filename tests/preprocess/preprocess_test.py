from fractions import Fraction

from src.preprocess import preprocess
from src.representation import preprocessed_lines_to_string

def test_preprocess_ntoles():
    """
    # Test n-toles

    Tested music:
    X: 1
    L: 1/8
    M: 3/4
    V: 1 clef=treble
    K: Bb
    [V:1] |(5::2 c2e3 & z2 & (3 C^c''_c,,, || d4 &z4& [abce]3 c :|
    """
    #quintole + 3 voices in a staff... 
    lines = [{"staff":[{"voices":[[{"el_type":"stem","direction":"up"},{"type":"bar_thin","el_type":"bar"},{"startTriplet":5,"tripletMultiplier":0.4,"tripletR":2,"pitches":[{"pitch":7,"name":"c","verticalPos":7,"highestVert":13}],"duration":0.25,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.375,"endTriplet":True,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"el_type":"stem","direction":"up"},{"el_type":"stem","direction":"auto"},{"type":"bar_thin_thin","el_type":"bar"},{"pitches":[{"pitch":8,"name":"d","verticalPos":8,"highestVert":8}],"duration":0.5,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"type":"bar_right_repeat","el_type":"bar"},{"el_type":"stem","direction":"auto"}],[{"el_type":"stem","direction":"down"},{"el_type":"stem","direction":"up"},{"type":"bar_thin","el_type":"bar"},{"rest":{"type":"rest"},"duration":0.25,"el_type":"note","averagepitch":11,"minpitch":11,"maxpitch":11},{"el_type":"stem","direction":"up"},{"el_type":"stem","direction":"auto"},{"type":"bar_thin_thin","el_type":"bar"},{"rest":{"type":"rest"},"duration":0.5,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"type":"bar_right_repeat","el_type":"bar"},{"el_type":"stem","direction":"auto"}],[{"el_type":"stem","direction":"down"},{"el_type":"stem","direction":"down"},{"type":"bar_thin","el_type":"bar"},{"startTriplet":3,"tripletMultiplier":0.6666666666666666,"tripletR":3,"pitches":[{"pitch":0,"name":"C","verticalPos":0,"highestVert":0}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":0,"minpitch":0,"maxpitch":0},{"pitches":[{"accidental":"sharp","pitch":21,"name":"^c''","verticalPos":21,"highestVert":21}],"duration":0.125,"el_type":"note","averagepitch":21,"minpitch":21,"maxpitch":21},{"pitches":[{"accidental":"flat","pitch":-14,"name":"_c,,,","verticalPos":-14,"highestVert":-14}],"duration":0.125,"endTriplet":True,"el_type":"note","endBeam":True,"averagepitch":-14,"minpitch":-14,"maxpitch":-14},{"type":"bar_thin_thin","el_type":"bar"},{"duration":0.375,"pitches":[{"pitch":7,"name":"c","verticalPos":7,"highestVert":7},{"pitch":9,"name":"e","verticalPos":9,"highestVert":9},{"pitch":12,"name":"a","verticalPos":12,"printer_shift":"different","highestVert":12},{"pitch":13,"name":"b","verticalPos":13,"highestVert":13}],"el_type":"note","averagepitch":10.25,"minpitch":7,"maxpitch":13},{"pitches":[{"pitch":7,"name":"c","verticalPos":7,"highestVert":7}],"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"type":"bar_right_repeat","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"flat","note":"B","verticalPos":6},{"acc":"flat","note":"e","verticalPos":9}],"root":"B","acc":"b","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"3","den":"4"}],"el_type":"timeSignature"}}]}]
    output = preprocess(lines)[0]
    print(output)
    print(preprocessed_lines_to_string(output))
    expected_output = [[[{'pitches': [{'pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 10)}, {'pitches': [{'pitch': 2, 'acc': 'flat'}], 'duration': Fraction(3, 20)}, {'pitches': [{'pitch': 1, 'acc': 'none'}], 'duration': Fraction(1, 2)}], [{'pitches': [], 'duration': Fraction(1, 4)}, {'pitches': [], 'duration': Fraction(1, 2)}], [{'pitches': [{'pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 12)}, {'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(1, 12)}, {'pitches': [{'pitch': 0, 'acc': 'flat'}], 'duration': Fraction(1, 12)}, {'pitches': [{'pitch': 0, 'acc': 'none'}, {'pitch': 2, 'acc': 'flat'}, {'pitch': 5, 'acc': 'none'}, {'pitch': 6, 'acc': 'flat'}], 'duration': Fraction(3, 8)}, {'pitches': [{'pitch': 0, 'acc': 'none'}], 'duration': Fraction(1, 8)}]]]
    assert output == expected_output


def test_preprocess_accidental_resolution():
    """
    # Test accidental resolution

    Tested music:
    X: 1
    L: 1/4
    M: 3/4
    K: D
    %%score (1 2)
    V:1 clef=treble
    V:2 clef=treble
    [V:1] |f2 e | ^d e f |
    [V:2] | _F A F | F A c/2 d/2 |
    """
    lines = [{"staff":[{"voices":[[{"el_type":"stem","direction":"up"},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.5,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"accidental":"sharp","pitch":8,"name":"^d","verticalPos":8,"highestVert":14}],"duration":0.25,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.25,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"type":"bar_thin","el_type":"bar"}],[{"direction":"down","el_type":"stem"},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"accidental":"flat","pitch":3,"name":"_F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":5,"name":"A","verticalPos":5,"highestVert":5}],"duration":0.25,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":5,"name":"A","verticalPos":5,"highestVert":5}],"duration":0.25,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":7,"name":"c","verticalPos":7,"highestVert":7}],"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":8,"name":"d","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7}],"root":"D","acc":"","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"3","den":"4"}],"el_type":"timeSignature"}}]}]
    print(lines)
    output = preprocess(lines)[0]
    print(output)
    print(preprocessed_lines_to_string(output))
    expected_output = [[[{'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 2)}, {'pitches': [{'pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 1, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}], [{'pitches': [{'pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 5, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 5, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 1, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}]]]
    assert output == expected_output

def test_preprocess_accidental_resolution_with_chords():
    """
    # Test accidental resolution

    Tested music:
    X: 1
    L: 1/4
    M: 3/4
    K: D
    %%score (1 2)
    V:1 clef=treble
    V:2 clef=treble
    [V:1] |f2 e | ^d e f |
    [V:2] | _F A F | F [=cF] c/2 d/2 |
    """
    lines = [{"staff":[{"voices":[[{"el_type":"stem","direction":"up"},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.5,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"accidental":"sharp","pitch":8,"name":"^d","verticalPos":8,"highestVert":14}],"duration":0.25,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.25,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"type":"bar_thin","el_type":"bar"}],[{"direction":"down","el_type":"stem"},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"accidental":"flat","pitch":3,"name":"_F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":5,"name":"A","verticalPos":5,"highestVert":5}],"duration":0.25,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"duration":0.25,"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3},{"accidental":"natural","pitch":7,"name":"=c","verticalPos":7,"highestVert":7}],"el_type":"note","averagepitch":5,"minpitch":3,"maxpitch":7},{"pitches":[{"pitch":7,"name":"c","verticalPos":7,"highestVert":7}],"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":8,"name":"d","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7}],"root":"D","acc":"","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"3","den":"4"}],"el_type":"timeSignature"}}]}]
    print(lines)
    output = preprocess(lines)[0]
    print(output)
    print(preprocessed_lines_to_string(output))
    expected_output = [[[{'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 2)}, {'pitches': [{'pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 1, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}], [{'pitches': [{'pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 5, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}, {'pitch': 0, 'acc': 'natural'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 0, 'acc': 'natural'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 1, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}]]]
    assert output == expected_output

def test_preprocess_add_key_accidentals():
    """
    # Test that key accidentals are added, but accidentals of one note are not added to other notes, even in the same bar.

    Tested music:
    X: 1
    L: 1/4
    M: 3/4
    K: D
    %%score (1 2)
    V:1 clef=treble
    V:2 clef=treble
    [V:1] f2 e ^d e | _f/2 f/2 |
    [V:2]  _F A F F A c/2 d/2|
    """
    lines = [{"staff":[{"voices":[[{"el_type":"stem","direction":"up"},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.5,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"accidental":"sharp","pitch":8,"name":"^d","verticalPos":8,"highestVert":14}],"duration":0.25,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"accidental":"flat","pitch":10,"name":"_f","verticalPos":10,"highestVert":16}],"duration":0.125,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.125,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"type":"bar_thin","el_type":"bar"}],[{"direction":"down","el_type":"stem"},{"pitches":[{"accidental":"flat","pitch":3,"name":"_F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":5,"name":"A","verticalPos":5,"highestVert":5}],"duration":0.25,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":5,"name":"A","verticalPos":5,"highestVert":5}],"duration":0.25,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":7,"name":"c","verticalPos":7,"highestVert":7}],"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":8,"name":"d","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7}],"root":"D","acc":"","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"3","den":"4"}],"el_type":"timeSignature"}}]}]
    print(lines)
    output = preprocess(lines)[0]
    print(output)
    print(preprocessed_lines_to_string(output))
    expected_output = [[[{'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 2)}, {'pitches': [{'pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 1, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}], [{'pitches': [{'pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 5, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 5, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 1, 'acc': 'none'}], 'duration': Fraction(1, 8)}]]]
    assert output == expected_output

def test_preprocess_add_key_accidentals_with_chords():
    """
    # Test that key accidentals are added, but accidentals of one note are not added to other notes, even in the same bar.

    Tested music:
    X: 1
    L: 1/4
    M: 3/4
    K: D
    %%score (1 2)
    V:1 clef=treble
    V:2 clef=treble
    [V:1] f2 e ^d e | _f/2 f/2 |
    [V:2]  _F A F F [=cF] c/2 d/2|
    """
    lines = [{"staff":[{"voices":[[{"el_type":"stem","direction":"up"},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.5,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"accidental":"sharp","pitch":8,"name":"^d","verticalPos":8,"highestVert":14}],"duration":0.25,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"accidental":"flat","pitch":10,"name":"_f","verticalPos":10,"highestVert":16}],"duration":0.125,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.125,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"type":"bar_thin","el_type":"bar"}],[{"direction":"down","el_type":"stem"},{"pitches":[{"accidental":"flat","pitch":3,"name":"_F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":5,"name":"A","verticalPos":5,"highestVert":5}],"duration":0.25,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"duration":0.25,"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3},{"accidental":"natural","pitch":7,"name":"=c","verticalPos":7,"highestVert":7}],"el_type":"note","averagepitch":5,"minpitch":3,"maxpitch":7},{"pitches":[{"pitch":7,"name":"c","verticalPos":7,"highestVert":7}],"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":8,"name":"d","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7}],"root":"D","acc":"","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"3","den":"4"}],"el_type":"timeSignature"}}]}] 
    print(lines)
    output = preprocess(lines)[0]
    print(output)
    print(preprocessed_lines_to_string(output))
    expected_output = [[[{'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 2)}, {'pitches': [{'pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 1, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 2, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}], [{'pitches': [{'pitch': 3, 'acc': 'flat'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 5, 'acc': 'none'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}, {'pitch': 0, 'acc': 'natural'}], 'duration': Fraction(1, 4)}, {'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 1, 'acc': 'none'}], 'duration': Fraction(1, 8)}]]]
    assert output == expected_output

def test_preprocess_multiple_lines():
    """
    # multiple lines
    
    Tested music:
    X: 1
	L: 1/8
	M: 6/8
	V: 1 clef=treble
	V: 2 clef=treble
	V: 3 clef=bass octave=-2
	K: F#
	[V:1] | aaa a^^ga | c'3 g3 |
	[V:2] | fff fef | e3 e3 |
	[V:3] | f zz fga | c' zz c zz |
	[V:1] | ggg gfg | a6 |
	[V:2] | eee ede | f6 |
	[V:3] | c zz cde | f zz F zz |
    """
    lines = [{"staff":[{"voices":[[{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":12,"name":"a","verticalPos":12,"highestVert":12}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":12,"minpitch":12,"maxpitch":12},{"pitches":[{"pitch":12,"name":"a","verticalPos":12,"highestVert":12}],"duration":0.125,"el_type":"note","averagepitch":12,"minpitch":12,"maxpitch":12},{"pitches":[{"pitch":12,"name":"a","verticalPos":12,"highestVert":12}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":12,"minpitch":12,"maxpitch":12},{"pitches":[{"pitch":12,"name":"a","verticalPos":12,"highestVert":12}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":12,"minpitch":12,"maxpitch":12},{"pitches":[{"accidental":"dblsharp","pitch":11,"name":"^^g","verticalPos":11,"highestVert":11}],"duration":0.125,"el_type":"note","averagepitch":11,"minpitch":11,"maxpitch":11},{"pitches":[{"pitch":12,"name":"a","verticalPos":12,"highestVert":12}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":12,"minpitch":12,"maxpitch":12},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":14,"name":"c'","verticalPos":14,"highestVert":14}],"duration":0.375,"el_type":"note","averagepitch":14,"minpitch":14,"maxpitch":14},{"pitches":[{"pitch":11,"name":"g","verticalPos":11,"highestVert":11}],"duration":0.375,"el_type":"note","averagepitch":11,"minpitch":11,"maxpitch":11},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7},{"acc":"sharp","note":"g","verticalPos":11},{"acc":"sharp","note":"d","verticalPos":8},{"acc":"sharp","note":"A","verticalPos":5},{"acc":"sharp","note":"e","verticalPos":9}],"root":"F","acc":"#","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"6","den":"8"}],"el_type":"timeSignature"}},{"voices":[[{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":10}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":10}],"duration":0.125,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":10}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":10}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":9}],"duration":0.125,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":10}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":10,"minpitch":10,"maxpitch":10},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":9}],"duration":0.375,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":9}],"duration":0.375,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7},{"acc":"sharp","note":"g","verticalPos":11},{"acc":"sharp","note":"d","verticalPos":8},{"acc":"sharp","note":"A","verticalPos":5},{"acc":"sharp","note":"e","verticalPos":9}],"root":"F","acc":"#","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"6","den":"8"}],"el_type":"timeSignature"}},{"voices":[[{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":-4,"name":"f","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":-4,"name":"f","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":8,"minpitch":8,"maxpitch":8},{"pitches":[{"pitch":-3,"name":"g","verticalPos":9,"highestVert":9}],"duration":0.125,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":-2,"name":"a","verticalPos":10,"highestVert":10}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":10,"minpitch":10,"maxpitch":10},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":0,"name":"c'","verticalPos":12,"highestVert":12}],"duration":0.125,"el_type":"note","averagepitch":12,"minpitch":12,"maxpitch":12},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":-7,"name":"c","verticalPos":5,"highestVert":11}],"duration":0.125,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"bass","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":8},{"acc":"sharp","note":"c","verticalPos":5},{"acc":"sharp","note":"g","verticalPos":9},{"acc":"sharp","note":"d","verticalPos":6},{"acc":"sharp","note":"A","verticalPos":3},{"acc":"sharp","note":"e","verticalPos":7}],"root":"F","acc":"#","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"6","den":"8"}],"el_type":"timeSignature"}}]},{"staff":[{"voices":[[{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":11,"name":"g","verticalPos":11,"highestVert":11}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":11,"minpitch":11,"maxpitch":11},{"pitches":[{"pitch":11,"name":"g","verticalPos":11,"highestVert":11}],"duration":0.125,"el_type":"note","averagepitch":11,"minpitch":11,"maxpitch":11},{"pitches":[{"pitch":11,"name":"g","verticalPos":11,"highestVert":11}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":11,"minpitch":11,"maxpitch":11},{"pitches":[{"pitch":11,"name":"g","verticalPos":11,"highestVert":11}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":11,"minpitch":11,"maxpitch":11},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":10}],"duration":0.125,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":11,"name":"g","verticalPos":11,"highestVert":11}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":11,"minpitch":11,"maxpitch":11},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":12,"name":"a","verticalPos":12,"highestVert":12}],"duration":0.75,"el_type":"note","averagepitch":12,"minpitch":12,"maxpitch":12},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7},{"acc":"sharp","note":"g","verticalPos":11},{"acc":"sharp","note":"d","verticalPos":8},{"acc":"sharp","note":"A","verticalPos":5},{"acc":"sharp","note":"e","verticalPos":9}],"root":"F","acc":"#","mode":"","el_type":"keySignature"}},{"voices":[[{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":9}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":9}],"duration":0.125,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":9}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":9}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":8,"name":"d","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":9}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":9,"minpitch":9,"maxpitch":9},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":10}],"duration":0.75,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7},{"acc":"sharp","note":"g","verticalPos":11},{"acc":"sharp","note":"d","verticalPos":8},{"acc":"sharp","note":"A","verticalPos":5},{"acc":"sharp","note":"e","verticalPos":9}],"root":"F","acc":"#","mode":"","el_type":"keySignature"}},{"voices":[[{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":-7,"name":"c","verticalPos":5,"highestVert":11}],"duration":0.125,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":-7,"name":"c","verticalPos":5,"highestVert":5}],"duration":0.125,"el_type":"note","startBeam":True,"averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":-6,"name":"d","verticalPos":6,"highestVert":6}],"duration":0.125,"el_type":"note","averagepitch":6,"minpitch":6,"maxpitch":6},{"pitches":[{"pitch":-5,"name":"e","verticalPos":7,"highestVert":7}],"duration":0.125,"el_type":"note","endBeam":True,"averagepitch":7,"minpitch":7,"maxpitch":7},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":-4,"name":"f","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":-11,"name":"F","verticalPos":1,"highestVert":7}],"duration":0.125,"el_type":"note","averagepitch":1,"minpitch":1,"maxpitch":1},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"rest":{"type":"rest"},"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"bass","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":8},{"acc":"sharp","note":"c","verticalPos":5},{"acc":"sharp","note":"g","verticalPos":9},{"acc":"sharp","note":"d","verticalPos":6},{"acc":"sharp","note":"A","verticalPos":3},{"acc":"sharp","note":"e","verticalPos":7}],"root":"F","acc":"#","mode":"","el_type":"keySignature"}}]}]
    print(lines)
    output = preprocess(lines)[0]
    print(output)
    print(preprocessed_lines_to_string(output))
    expected_output = [[[{'pitches': [{'pitch': 5, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 5, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 5, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 5, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 4, 'acc': 'dblsharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 5, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(3, 8)}, {'pitches': [{'pitch': 4, 'acc': 'sharp'}], 'duration': Fraction(3, 8)}], [{'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(3, 8)}, {'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(3, 8)}], [{'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 4, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 5, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}]], [[{'pitches': [{'pitch': 4, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 4, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 4, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 4, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 4, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 5, 'acc': 'sharp'}], 'duration': Fraction(3, 4)}], [{'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 1, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(3, 4)}], [{'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 0, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 1, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 2, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [{'pitch': 3, 'acc': 'sharp'}], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}, {'pitches': [], 'duration': Fraction(1, 8)}]]]
    assert output == expected_output


def test_preprocess_information():
    """
    # Test accidental resolution

    Tested music:
    X: 1
    L: 1/4
    M: 3/4
    K: D
    %%score (1 2)
    V:1 clef=treble
    V:2 clef=treble
    [V:1] |f2 e | ^d e f |
    [V:2] | _F A F | F A c/2 d/2 |
    """
    lines = [{"staff":[{"voices":[[{"el_type":"stem","direction":"up"},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.5,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"accidental":"sharp","pitch":8,"name":"^d","verticalPos":8,"highestVert":14}],"duration":0.25,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"pitches":[{"pitch":9,"name":"e","verticalPos":9,"highestVert":15}],"duration":0.25,"el_type":"note","averagepitch":9,"minpitch":9,"maxpitch":9},{"pitches":[{"pitch":10,"name":"f","verticalPos":10,"highestVert":16}],"duration":0.25,"el_type":"note","averagepitch":10,"minpitch":10,"maxpitch":10},{"type":"bar_thin","el_type":"bar"}],[{"direction":"down","el_type":"stem"},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"accidental":"flat","pitch":3,"name":"_F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":5,"name":"A","verticalPos":5,"highestVert":5}],"duration":0.25,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"type":"bar_thin","el_type":"bar"},{"pitches":[{"pitch":3,"name":"F","verticalPos":3,"highestVert":3}],"duration":0.25,"el_type":"note","averagepitch":3,"minpitch":3,"maxpitch":3},{"pitches":[{"pitch":5,"name":"A","verticalPos":5,"highestVert":5}],"duration":0.25,"el_type":"note","averagepitch":5,"minpitch":5,"maxpitch":5},{"pitches":[{"pitch":7,"name":"c","verticalPos":7,"highestVert":7}],"duration":0.125,"el_type":"note","averagepitch":7,"minpitch":7,"maxpitch":7},{"pitches":[{"pitch":8,"name":"d","verticalPos":8,"highestVert":8}],"duration":0.125,"el_type":"note","averagepitch":8,"minpitch":8,"maxpitch":8},{"type":"bar_thin","el_type":"bar"}]],"clef":{"type":"treble","el_type":"clef"},"key":{"accidentals":[{"acc":"sharp","note":"f","verticalPos":10},{"acc":"sharp","note":"c","verticalPos":7}],"root":"D","acc":"","mode":"","el_type":"keySignature"},"meter":{"type":"specified","value":[{"num":"3","den":"4"}],"el_type":"timeSignature"}}]}]
    print(lines)
    output = preprocess(lines)[1]
    print(output)
    expected_output = ['The accidental_mode is "bar". Accidentals of a note in a bar now apply for all notes with the same octave_pitch after the note in the bar. The given key accidentals are applied, if there is no accidental in the bar for this pitch.']
    assert output == expected_output