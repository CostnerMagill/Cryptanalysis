import codecs
import string
from collections import Counter

class FrequencyAnalyzer:
    def __init__(self, file_path, encoding="utf-8"):
        self.file_path = file_path
        self.encoding = encoding

    def analyze(self):
        with open(self.file_path, "r", encoding=self.encoding) as file:
            text = file.read()

        # Convert text to lowercase
        text = text.lower()

        # Count single letters (one-grams)
        one_grams = Counter([og for og in [text[i:i+1] for i in range(len(text))] if all(c in string.ascii_letters for c in og)])

        # Count two-letter (bi-grams)
        bi_grams = Counter([bg for bg in [text[i:i+2] for i in range(len(text)-1)] if all(c in string.ascii_letters for c in bg)])

        # Count three-letter (tri-grams)
        tri_grams = Counter([tg for tg in [text[i:i+3] for i in range(len(text)-2)] if all(c in string.ascii_letters for c in tg)])

        return one_grams, bi_grams, tri_grams

file_path = "PA3support/Cryptanalysis/hamlet.txt"
encoding = "utf-8"  # Adjust this based on the actual encoding of the file
analyzer = FrequencyAnalyzer(file_path, encoding)
one_grams, bi_grams, tri_grams = analyzer.analyze()

# Print the results
print("One-grams:")
for letter, count in one_grams.most_common():
        print(f"{letter}: {count}")

print("\nTop 10 Bi-grams:")
for bi_gram, count in bi_grams.most_common(10):
        print(f"{bi_gram}: {count}")

print("\nTop 10 Tri-grams:")
for tri_gram, count in tri_grams.most_common(10):
        print(f"{tri_gram}: {count}")
