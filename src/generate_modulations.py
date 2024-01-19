



def modulations_in_chord_set(chordset):
    hps = all_possible_harmonic_states_with_path(chordset)
    
    hss = list(map(lambda x: x[0][1], hps))

    ms = modulations(hss, chordset)

    return ms


def all_possible_harmonic_states_with_path(chordset):
    pass




def modulations(hss, chordset):
    return [[(hs, pcset, calcNewHarmonicState(hs, pcset)) for hs in hss] for pcset in chordset]


