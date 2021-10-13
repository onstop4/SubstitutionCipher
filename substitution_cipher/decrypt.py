from argparse import ArgumentParser
import json


def parse_args():
    """
    Parses command line arguments.
    """
    parser = ArgumentParser()
    # Allows user to specify key file.
    parser.add_argument("-k", "--key", default="key.json")
    # Allows user to specify an input file and output file for decryption. If this
    # argument isn't used, then user will enter interactive prompt. See
    # "interactive" function for more details.
    parser.add_argument("-f", "--files", nargs=2, metavar=("ENCRYPTED", "DECRYPTED"))
    return parser.parse_args()


def reverse_dict(dictionary: dict):
    """
    Returns a dictionary where the keys and values in the provided argument have been
    swapped.
    """
    return {v: k for k, v in dictionary.items()}


def decrypt_text(text: str, key: dict) -> str:
    """
    Decrypts text by replacing each letter with its mapped value according to the key.
    Returns decrypted text.
    """
    result = []
    for character in text:
        shifted = key.get(character.lower())
        if shifted:
            result.append(shifted)

    return "".join(result)


def decrypt_file(input_filename: str, output_filename: str, key: dict):
    """
    Decrypts specified input file (using decrypt_text function) and writes result to
    specified output file.
    """
    with open(input_filename, encoding="utf8") as input_file:
        with open(output_filename, "w", encoding="utf8") as output_file:
            for line in input_file:
                output_file.write(decrypt_text(line, key) + "\n")


def interactive(key: dict):
    """
    Repeatedly prompts user to enter a line of text that will then be decrypted
    using decrypt_text function and then printed. Will quit when user enters "-1".
    """
    while True:
        text = input("Enter a string to decrypt (-1 to quit): ")
        if text == "-1":
            break
        print(decrypt_text(text, key))


def main():
    """
    Called when running this Python file as a script.
    """
    args = parse_args()

    with open(args.key) as key_file:
        # The dict needs to be reversed so that ciphertext letters can be used to look
        # up plaintext letters.
        key = reverse_dict(json.load(key_file))

    if args.files:
        decrypt_file(args.files[0], args.files[1], key)
    else:
        interactive(key)


if __name__ == "__main__":
    main()
