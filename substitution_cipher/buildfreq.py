from argparse import ArgumentParser
from collections import Counter
from string import ascii_lowercase


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("input")
    return parser.parse_args()


def count_chars_in_file(input_filename: dict):
    counter = Counter()

    with open(input_filename, encoding="utf8") as input_file:
        for line in input_file:
            counter.update(line.lower())

    return counter


def get_letter_frequency(char_counter: Counter):
    letter_count = {}
    total = 0

    for letter in ascii_lowercase:
        count = char_counter[letter]
        letter_count[letter] = count
        total += count

    # OrderedDict is not needed since dicts preserve order since Python 3.7.
    return {k: v / total for k, v in letter_count.items()}


def main():
    args = parse_args()

    counter = count_chars_in_file(args.input)
    letter_freq = get_letter_frequency(counter)

    for k, v in letter_freq.items():
        print("{} : {:.5f}".format(k, v))


if __name__ == "__main__":
    main()
