from src.type import parse_harmonic_state, all_keys

def test_parse_harmonic_state():
    assert parse_harmonic_state('[All]') == all_keys
    assert parse_harmonic_state('[]') == []
    assert parse_harmonic_state('[Bbm]') == [(10, 'moll')]
    assert parse_harmonic_state('[C, D, Em]') == [(0, 'dur'), (2, 'dur'), (4, 'moll')]