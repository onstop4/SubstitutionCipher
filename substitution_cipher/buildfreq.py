from argparse import ArgumentParser
from collections import Counter
from string import ascii_lowercase


def parse_args():
    """
    Parses command line arguments.
    """
    parser = ArgumentParser()
    parser.add_argument("--fast", action="store_true")
    # User must specify input file.
    parser.add_argument("input")
    return parser.parse_args()


def count_chars_in_file(input_filename: str, line_by_line: bool = True) -> Counter:
    """
    Iterates line-by-line through specified file and counts the characters present in
    each line. Returns resulting Counter. All letters (uppercase and lowercase) are
    counted as lowercase letters. The parameter line_by_line determines whether to read
    the file line-by-line (the default) or to read it all at once.
    """
    counter = Counter()

    with open(input_filename, encoding="utf8") as input_file:
        if line_by_line:
            for line in input_file:
                counter.update(line.lower())
        else:
            counter.update(input_file.read().lower())

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

    # Will read entire input file if "--fast" is passed.
    # Otherwise, input file will be read line-by-line.
    counter = count_chars_in_file(args.input, not args.fast)
    letter_freq = get_letter_frequency(counter)

    # Sorts output based on frequencies, so highest frequency letter will come last.
    for k, v in sorted(letter_freq.items(), key=lambda kv: kv[1]):
        # Prints letter and frequency up to fifth decimal place.
        print("{} : {:.5f}".format(k, v))


if __name__ == "__main__":
    main()
