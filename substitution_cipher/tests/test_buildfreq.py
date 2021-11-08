from collections import Counter, namedtuple
from string import ascii_lowercase

from substitution_cipher.buildfreq import count_chars_in_file, get_letter_frequency

# Samples for testing count_chars_in_file.
samples = {"abcabc. def": Counter("abcabc. def")}

lowercase = set(ascii_lowercase)

LetterCountSample = namedtuple("LetterCountSample", ["total", "letters"])

# Samples for testing get_letter_frequency.
letter_count_samples = {
    "abcabc. def": LetterCountSample(
        9, {"a": 2, "b": 2, "c": 2, "d": 1, "e": 1, "f": 1}
    ),
    "123dddeef": LetterCountSample(6, {"d": 3, "e": 2, "f": 1}),
}

# Adds missing letters to letter count samples.
for letter_count in letter_count_samples.values():
    letters = letter_count.letters
    not_present = lowercase - letters.keys()
    for letter in not_present:
        letters[letter] = 0


def test_count_chars_in_file_line_by_line(tmpdir):
    """
    Tests :py:func:`substitution_cipher.buildfreq.count_chars_in_file` when it counts
    the characters in a file line-by-line.
    """
    input_filename = tmpdir.join("input.txt")

    for k, v in samples.items():
        with open(input_filename, "w", encoding="utf8") as input_file:
            input_file.write(k)

        assert v == count_chars_in_file(input_filename, True)


def test_count_chars_in_file_all_at_once(tmpdir):
    """
    Tests :py:func:`substitution_cipher.buildfreq.count_chars_in_file` when it counts
    the characters in a file all at once (rather than line-by-line).
    """
    input_filename = tmpdir.join("input.txt")

    for k, v in samples.items():
        with open(input_filename, "w", encoding="utf8") as input_file:
            input_file.write(k)

        assert v == count_chars_in_file(input_filename, False)


def test_get_letter_frequency():
    """
    Tests :py:func:`substitution_cipher.buildfreq.get_letter_frequency`.
    """
    for k, v in samples.items():
        letter_freq = get_letter_frequency(v)
        assert len(letter_freq) == 26
        letter_count = letter_count_samples[k]
        assert letter_freq == {
            k: v / letter_count.total for k, v in letter_count.letters.items()
        }
