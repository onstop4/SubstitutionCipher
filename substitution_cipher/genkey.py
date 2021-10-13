from argparse import ArgumentParser
import json
from random import SystemRandom
import string

# Secure random number generator.
system_random = SystemRandom()


def parse_args():
    """
    Parses command line arguments.
    """
    parser = ArgumentParser()
    # Allows user to specify output file.
    parser.add_argument("-o", "--output", default="key.json")
    return parser.parse_args()


def generate_key() -> dict:
    """
    Generates a key (in the form of a dict) that for encryption/descryption using the
    substitution cipher.
    """
    key = {}
    scrambled_letters = system_random.sample(string.ascii_lowercase, k=26)

    # Maps plaintext letters to ciphertext letters.
    for index, letter in enumerate(string.ascii_lowercase):
        key[letter] = scrambled_letters[index]

    return key


def main():
    """
    Called when running this Python file as a script.
    """
    args = parse_args()
    filename = args.output

    key = generate_key()
    with open(filename, "w") as file:
        json.dump(key, file)
    print("Outputted key to {}".format(filename))


if __name__ == "__main__":
    main()
