from argparse import ArgumentParser
from collections import Counter
from string import ascii_lowercase


def parse_args():
    """
    Parses command line arguments.
    """
    parser = ArgumentParser()
    # User must specify input file.
    parser.add_argument("input")
    return parser.parse_args()


def count_chars_in_file(input_filename: str) -> Counter:
    """
    Iterates line-by-line through specified file and counts the characters present in
    each line. Returns resulting Counter. All letters (uppercase and lowercase) are
    counted as lowercase letters.
    """
    counter = Counter()

    with open(input_filename, encoding="utf8") as input_file:
        for line in input_file:
            counter.update(line.lower())

    return counter


def get_letter_frequency(char_counter: Counter) -> dict:
    """
    Returns dict mapping letters to their specific frequencies (as decimals).
    """
    letter_count = {}
    total = 0

    for letter in ascii_lowercase:
        count = char_counter[letter]
        letter_count[letter] = count
        total += count

    # OrderedDict is not needed since dicts preserve order since Python 3.7.
    return {k: v / total for k, v in letter_count.items()}


def main():
    """
    Called when running this Python file as a script.
    """
    args = parse_args()

    counter = count_chars_in_file(args.input)
    letter_freq = get_letter_frequency(counter)

    # Sorts output based on frequencies, so highest frequency letter will come last.
    for k, v in sorted(letter_freq.items(), key=lambda kv: kv[1]):
        # Prints letter and frequency up to fifth decimal place.
        print("{} : {:.5f}".format(k, v))


if __name__ == "__main__":
    main()
