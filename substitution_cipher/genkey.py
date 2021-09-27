from argparse import ArgumentParser
import json
from random import SystemRandom
import string

# Secure random number generator.
system_random = SystemRandom()


def generate_key():
    key = {}
    letters_available = list(system_random.sample(string.ascii_uppercase, k=26))

    for index, letter in enumerate(string.ascii_lowercase):
        key[letter] = letters_available[index]

    return key


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-o", "--output", default="key.json")
    return parser.parse_args()


def main():
    args = parse_args()
    filename = args.output

    key = generate_key()
    with open(filename, "w") as file:
        json.dump(key, file)
    print("Outputted key to {}".format(filename))


if __name__ == "__main__":
    main()
