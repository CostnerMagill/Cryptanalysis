import string
from collections import Counter
import os


def freq_analyze(file_paths):
    """
    Analyze the letter frequencies in the given text files.

    Ignores case and prints the following:
    - All non-zero counts of single letters (one-grams) in decreasing order.
    - The 10 highest non-zero counts of two-letter (bi-grams) in decreasing order.
    - The 10 highest non-zero counts of three-letter (tri-grams) in decreasing order.
    """
    total_text = ""
    for file_path in file_paths:
        with open(file_path, "r") as file:
            text = file.read()
            total_text += text

    # Convert text to lowercase
    total_text = total_text.lower()

    # Count single letters (one-grams)
    one_grams = Counter(total_text)

    # Count two-letter (bi-grams)
    bi_grams = Counter([total_text[i:i + 2] for i in range(len(total_text) - 1)])

    # Count three-letter (tri-grams)
    tri_grams = Counter([total_text[i:i + 3] for i in range(len(total_text) - 2)])

    # Print one-grams
    print("One-grams:")
    for letter, count in one_grams.most_common():
        if letter in string.ascii_lowercase:
            print(f"{letter}: {count}")

    # Print top 10 bi-grams
    print("\nTop 10 Bi-grams:")
    for bi_gram, count in bi_grams.most_common(10):
        print(f"{bi_gram}: {count}")

    # Print top 10 tri-grams
    print("\nTop 10 Tri-grams:")
    for tri_gram, count in tri_grams.most_common(10):
        print(f"{tri_gram}: {count}")


# Example usage
file_paths = [
    # "PA3support/Cryptanalysis/ciphertext.txt"
    # "PA3support/Cryptanalysis/hamlet.txt"
    "PA3support/Cryptanalysis/merchantofvenice.txt"
]
freq_analyze(file_paths)
