from argparse import ArgumentParser
import json


def encrypt_text(text, key):
    result = []

    for character in text:
        shifted = key.get(character.lower())
        if shifted:
            result.append(shifted)

    return "".join(result)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-k", "--key", default="key.json")
    parser.add_argument("-f", "--files", nargs=2, metavar=("ORIGINAL", "ENCRYPTED"))
    return parser.parse_args()


def encrypt_file(input_filename, output_filename, key):
    with open(input_filename, encoding="utf8") as input_file:
        with open(output_filename, "w", encoding="utf8") as output_file:
            for line in input_file:
                output_file.write(encrypt_text(line, key) + "\n")


def interactive(key):
    while True:
        text = input("Enter a string to encrypt (-1 to quit): ")
        if text == "-1":
            break
        print(encrypt_text(text, key))


def main():
    args = parse_args()

    with open(args.key) as key_file:
        key = json.load(key_file)

    if args.files:
        encrypt_file(args.files[0], args.files[1], key)
    else:
        interactive(key)


if __name__ == "__main__":
    main()
