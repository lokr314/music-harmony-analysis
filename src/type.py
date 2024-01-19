from typing import List, Tuple
from fractions import Fraction

def powerset(lst: List) -> List[List]:
    print(lst)
    if not lst:
        return [[]]
    ps = powerset(lst[1:])
    return ps + [x + [lst[0]] for x in ps]

PC = int
all_PCs: List[PC] = list(range(12))

PCSet = List[PC]

Key = Tuple[PC, str]
all_keys: List[Key] = [(n, mode) for n in range(12) for mode in ['dur', 'moll']]

HarmonicState = List[Key]
#all_harmonic_states: List[HarmonicState] = [hs for hs in powerset(all_keys) if len(hs) < 15] # This takes waaaaay to long

HarmonicEvent = Tuple[PCSet, Fraction]
Music = List[HarmonicEvent]
HarmonicAnalysis = List[Tuple[HarmonicEvent, HarmonicState]]

dur = [0, 2, 4, 5, 7, 9, 11]
moll = [0, 2, 3, 5, 7, 8, 11]

def show_key(key: Key) -> str:
    """
    Input:
    - key: tupel with two fields: pitchclass: int from 0-11 and mode: 'dur' or 'moll'

    Output:
    The Key as a string in the format 'C' for dur and 'Am' for moll. Fis and Es are used for sharp and flat keys.
    Bb is used for pitchclass 10, B for pitchclass 11.
    
    Example:
    (0, 'dur') -> 'C'
    (1, 'dur') -> 'Cis'
    (1, 'moll') -> 'Cism'
    (11, 'moll') -> 'Bm'
    (10, 'dur') -> 'Bb'
    """
    n, mode = key
    notes = ['C', 'Cis', 'D', 'Es', 'E', 'F', 'Fis', 'G', 'As', 'A', 'Bb', 'B']
    return notes[n] + ('' if mode == 'dur' else 'm')

def show_harmonic_state(keys: HarmonicState) -> str:
    if not keys:
        return "[]"
    return "[" + ", ".join([show_key(key) for key in keys]) + "]"

def show_harmonic_states(states: List[HarmonicState]) -> str:
    return "".join([show_harmonic_state(state) for state in states])

def key_to_pcset(key: Key) -> PCSet:
    n, mode = key
    return transpose(n, dur) if mode == 'dur' else transpose(n, moll)

def show_harmonic_analysis(analysis: HarmonicAnalysis) -> str:
    return "\n".join([f"{pcset} {duration} {keys}" for (pcset, duration), keys in analysis])


def transpose(n: int, pcset: PCSet) -> PCSet:
    return [(pc + n) % 12 for pc in pcset]
