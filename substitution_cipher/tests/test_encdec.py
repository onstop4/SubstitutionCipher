from substitution_cipher.decrypt import decrypt_file, decrypt_text, reverse_dict
from substitution_cipher.encrypt import encrypt_file, encrypt_text

key = {
    "a": "x",
    "b": "b",
    "c": "r",
    "d": "z",
    "e": "a",
    "f": "y",
    "g": "j",
    "h": "m",
    "i": "c",
    "j": "d",
    "k": "o",
    "l": "u",
    "m": "n",
    "n": "e",
    "o": "t",
    "p": "q",
    "q": "h",
    "r": "w",
    "s": "g",
    "t": "l",
    "u": "k",
    "v": "f",
    "w": "p",
    "x": "i",
    "y": "s",
    "z": "v",
}

reversed_key = {
    "x": "a",
    "b": "b",
    "r": "c",
    "z": "d",
    "a": "e",
    "y": "f",
    "j": "g",
    "m": "h",
    "c": "i",
    "d": "j",
    "o": "k",
    "u": "l",
    "n": "m",
    "e": "n",
    "t": "o",
    "q": "p",
    "h": "q",
    "w": "r",
    "g": "s",
    "l": "t",
    "k": "u",
    "f": "v",
    "p": "w",
    "i": "x",
    "s": "y",
    "v": "z",
}

encryption_samples = {
    "this is A test Message 12345 done.": "lmcgcgxlaglnaggxjaztea",
    "?haha": "mxmx",
    "...echo ...I": "armtc",
}

decryption_samples = {
    "LMC2GCGXL3AGL NAGGXJAZTEA": "thisisatestmessagedone",
    "? MXMX": "haha",
    "ARM12345TC": "echoi",
}


def test_reverse_dict():
    assert reverse_dict(key) == reversed_key


class TestHandleText:
    def test_encrypt_text(self):
        for original, encrypted in encryption_samples.items():
            assert encrypt_text(original, key) == encrypted

    def test_decrypt_text(self):
        for encrypted, decrypted in decryption_samples.items():
            assert decrypt_text(encrypted, reversed_key) == decrypted


class TestHandleFiles:
    def test_encrypt_file(self, tmpdir):
        input_filename = tmpdir.join("input.txt")
        output_filename = tmpdir.join("output.txt")

        with open(input_filename, "w") as input_file:
            input_file.write("\n".join(encryption_samples.keys()))

        encrypt_file(input_filename, output_filename, key)

        expected = "\n".join(encryption_samples.values()) + "\n"
        with open(output_filename) as output_file:
            assert output_file.read() == expected

    def test_decrypt_file(self, tmpdir):
        input_filename = tmpdir.join("input.txt")
        output_filename = tmpdir.join("output.txt")

        with open(input_filename, "w") as input_file:
            input_file.write("\n".join(decryption_samples.keys()))

        decrypt_file(input_filename, output_filename, reversed_key)

        expected = "\n".join(decryption_samples.values()) + "\n"
        with open(output_filename) as output_file:
            assert output_file.read() == expected
