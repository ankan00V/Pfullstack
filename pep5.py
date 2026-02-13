import sys
import re

lines = sys.stdin.read().splitlines()
first = lines[0] if len(lines) > 0 else ""
second = lines[1] if len(lines) > 1 else ""

def clean(s):
    return re.findall(r"[A-Za-z]+", s)

tokens = clean(first) + clean(second)

word_to_id = {}
id_to_word = []
encoded = []

for w in tokens:
    if w not in word_to_id:
        word_to_id[w] = len(id_to_word)
        id_to_word.append(w)
    encoded.append(word_to_id[w])

print(" ".join(str(x) for x in encoded))
print(" ".join(id_to_word))
