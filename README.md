# Substitution Cipher Assignment
These were the scripts I submitted for my substitution cipher assignment. They were written for (and tested using) Python 3.9. The scripts are meant to encrypt/decrypt UTF-8 text files or standard input, substituting plaintext English letters with ciphertext English letters.

Please note that the instructions under the Encryption and Decryption sections require a key file to be generated beforehand. To generate a key file, please see the section below titled "Generating a Key".

## Dependencies
The scripts don't require anything except Python 3.9+ to run. The packages in `requirements.txt` are only needed for testing (via Pytest) and code formatting (via Black).

## Generating a Key
To generate a key, run `python3 substitution_cipher/keygen.py`. This will generate a key file in the current directory called "key.json". If you want the key file stored somewhere else, then run `python3 substitution_cipher/keygen.py -o {KEYFILE}`, replacing `{KEYFILE}` with the location of the key file.

## Encryption
The encryption process involves using the encrypt.py script. By default, it uses a key file in the current direction called "key.json". If the key file is stored somewhere else, append `-k {KEYFILE}` to the end of the commands used in the sections below, replacing `{KEYFILE}` with the path to the key file.

### Encrypting Standard Input
To encrypt standard input, run `python3 substitution_cipher/encrypt.py`. This allow you to enter lines of plaintext that will be immediately encrypted and outputted. To exit the script, enter "-1" (that's negative one) into the prompt exactly.

### Encrypting A File
To encrypt a file and output the ciphertext to another file, run `python3 substitution_cipher/encrypt.py -f {INPUTFILE} {OUTPUTFILE}`, replacing `{INPUTFILE}` with the path of the input file and `{OUTPUTFILE}` with the path of the output file (which the ciphertext will be outputted to).

## Decryption
The decryption process involves using the decrypt.py script. By default, it uses a key file in the current direction called "key.json". If the key file is stored somewhere else, append `-k {KEYFILE}` to the end of the commands used in the sections below, replacing `{KEYFILE}` with the path to the key file.

### Decrypting Standard Input
To decrypt standard input, run `python3 substitution_cipher/decrypt.py`. This allow you to enter lines of ciphertext that will be immediately decrypted and outputted. To exit the script, enter "-1" into the prompt exactly.

### Decrypting A File
To decrypt a file and output the plaintext to another file, run `python3 substitution_cipher/decrypt.py -f {INPUTFILE} {OUTPUTFILE}`, replacing `{INPUTFILE}` with the path of the input file and `{OUTPUTFILE}` with the path of the output file (which the plaintext will be outputted to).

## Determining Letter Frequency
To determine the English letter frequency of a text file, run `python3 substitution_cipher/buildfreq.py {INPUTFILE}`, replacing `{INPUTFILE}` with the path to the input file. It will output a report of the frequency of each English letter. By default, the buildfreq.py script reads the input file line-by-line. To read the input file all at once (which is much faster if the file is large), run `python3 substitution_cipher/buildfreq.py --fast {INPUTFILE}` instead. Please note that the `--fast` argument will cause the script to use an amount of RAM that's twice as large as the input file, so make sure you have enough memory before using that argument.
