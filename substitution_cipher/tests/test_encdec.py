from substitution_cipher.decrypt import decrypt_file, decrypt_text, reverse_dict
from substitution_cipher.encrypt import encrypt_file, encrypt_text

key = {
    "a": "X",
    "b": "B",
    "c": "R",
    "d": "Z",
    "e": "A",
    "f": "Y",
    "g": "J",
    "h": "M",
    "i": "C",
    "j": "D",
    "k": "O",
    "l": "U",
    "m": "N",
    "n": "E",
    "o": "T",
    "p": "Q",
    "q": "H",
    "r": "W",
    "s": "G",
    "t": "L",
    "u": "K",
    "v": "F",
    "w": "P",
    "x": "I",
    "y": "S",
    "z": "V",
}

reversed_key = {
    "X": "a",
    "B": "b",
    "R": "c",
    "Z": "d",
    "A": "e",
    "Y": "f",
    "J": "g",
    "M": "h",
    "C": "i",
    "D": "j",
    "O": "k",
    "U": "l",
    "N": "m",
    "E": "n",
    "T": "o",
    "Q": "p",
    "H": "q",
    "W": "r",
    "G": "s",
    "L": "t",
    "K": "u",
    "F": "v",
    "P": "w",
    "I": "x",
    "S": "y",
    "V": "z",
}

encryption_samples = {
    "this is A test Message 12345 done.": "LMCGCGXLAGLNAGGXJAZTEA",
    "?haha": "MXMX",
    "...echo ...I": "ARMTC",
}

decryption_samples = {
    "LMC2GCGXL3AGL NAGGXJAZTEA": "thisisatestmessagedone",
    "? MXMX": "haha",
    "ARM12345TC": "echoi",
}


def test_reverse_dict():
    """
    Tests :py:func:`substitution_cipher.decrypt.reverse_dict`.
    """
    assert reverse_dict(key) == reversed_key


class TestHandleText:
    """
    Tests the encryption/decryption of strings.
    """

    def test_encrypt_text(self):
        """
        Tests :py:func:`substitution_cipher.encrypt.encrypt_text`.
        """
        for original, encrypted in encryption_samples.items():
            assert encrypt_text(original, key) == encrypted

    def test_decrypt_text(self):
        """
        Tests :py:func:`substitution_cipher.decrypt.decrypt_text`.
        """
        for encrypted, decrypted in decryption_samples.items():
            assert decrypt_text(encrypted, reversed_key) == decrypted


class TestHandleFiles:
    """
    Tests the encryption/decryption of plaintext (UTF-8) files.
    """

    def test_encrypt_file(self, tmpdir):
        """
        Tests :py:func:`substitution_cipher.encrypt.encrypt_file`.
        """
        input_filename = tmpdir.join("input.txt")
        output_filename = tmpdir.join("output.txt")

        with open(input_filename, "w", encoding="utf8") as input_file:
            input_file.write("\n".join(encryption_samples.keys()))

        encrypt_file(input_filename, output_filename, key)

        expected = "\n".join(encryption_samples.values()) + "\n"
        with open(output_filename, encoding="utf8") as output_file:
            assert output_file.read() == expected

    def test_decrypt_file(self, tmpdir):
        """
        Tests :py:func:`substitution_cipher.decrypt.decrypt_file`.
        """
        input_filename = tmpdir.join("input.txt")
        output_filename = tmpdir.join("output.txt")

        with open(input_filename, "w", encoding="utf8") as input_file:
            input_file.write("\n".join(decryption_samples.keys()))

        decrypt_file(input_filename, output_filename, reversed_key)

        expected = "\n".join(decryption_samples.values()) + "\n"
        with open(output_filename, encoding="utf8") as output_file:
            assert output_file.read() == expected
