from argparse import ArgumentParser
import json


def reverse_dict(dictionary):
    return {v: k for k, v in dictionary.items()}


def decrypt_text(text, key):
    result = []
    for character in text:
        shifted = key.get(character.upper())
        if shifted:
            result.append(shifted)

    return "".join(result)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-k", "--key", default="key.json")
    parser.add_argument("-f", "--files", nargs=2, metavar=("ENCRYPTED", "DECRYPTED"))
    return parser.parse_args()


def decrypt_file(input_filename, output_filename, key):
    with open(input_filename) as input_file:
        with open(output_filename, "w") as output_file:
            for line in input_file:
                output_file.write(decrypt_text(line, key) + "\n")


def interactive(key):
    while True:
        text = input("Enter a string to decrypt (-1 to quit): ")
        if text == "-1":
            break
        print(decrypt_text(text, key))


def main():
    args = parse_args()

    with open(args.key) as key_file:
        key = reverse_dict(json.load(key_file))

    if args.files:
        decrypt_file(args.files[0], args.files[1], key)
    else:
        interactive(key)


if __name__ == "__main__":
    main()
