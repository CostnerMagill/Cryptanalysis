import argparse
import inspect
import os
import string

# Define the cipher mapping
cipher_map = {
    'M': 'A', 'F': 'B', 'A': 'C', 'N': 'D', 'X': 'E', 'I': 'F', 'W': 'G', 'P': 'H',
    'B': 'I', 'S': 'J', 'H': 'K', 'G': 'L', 'L': 'M', 'T': 'N', 'C': 'O', 'Q': 'P',
    'K': 'Q', 'V': 'R', 'R': 'S', 'J': 'T', 'U': 'U', 'D': 'V', 'Y': 'W', 'Z': 'X',
    'E': 'Y', 'O': 'Z'
}

script_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--txt_file', default = os.path.join(script_dir, 'ciphertext.txt'), help = 'Path of .txt file to decipher')
args = parser.parse_args()


class decipher:
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def decipher_text(self):
        with open(self.file_path, "r", encoding=self.encoding) as file:
            text = file.read()
        plaintext = ""
        for char in text:
            if char.upper() in cipher_map:
                if char.isupper():
                    plaintext += cipher_map[char]
                else:
                    plaintext += cipher_map[char.upper()].lower()
            else:
                plaintext += char
        return plaintext


file_path = args.txt_file
print("File to Decipher: " + file_path)
encoding = "utf-8"  # Adjust this based on the actual encoding of the file
deciphered = decipher(file_path, encoding)
# Decipher the ciphertext
decipheredText = deciphered.decipher_text()


# Print the codebook and the deciphered plaintext
print("Codebook:")
for key, value in cipher_map.items():
    print(f"{key} -> {value}")
print("\nDeciphered Plaintext:")
print(decipheredText)
