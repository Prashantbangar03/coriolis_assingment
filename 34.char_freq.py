import re


def char_freq_table(filepath):
    file = open(filepath)
    chars = file.read().lower().replace(" ", "").replace("\n", "")
    freqs = {key: 0 for key in chars}
    for char in chars:
        freqs[char] += 1
    for word in freqs:
        print ("%s: %s" % (word, freqs[word]))


if __name__ == "__main__":
    char_freq_table('pallindrom_version.py')
