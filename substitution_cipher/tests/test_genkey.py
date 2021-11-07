from substitution_cipher.genkey import generate_key


def test_generate_key():
    """
    Tests :py:func:`substitution_cipher.genkey.generate_key`.
    """
    key = generate_key()

    assert len(key) == 26

    keys = list(key.keys())
    values = list(key.values())

    for k, v in key.items():
        assert keys.count(k) == 1
        assert values.count(v) == 1
