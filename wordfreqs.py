from collections import Counter

# Assuming enwik6 is a plain text file
with open('enwik6.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Split text into words
words = text.split()

# Count word frequencies
word_freqs = Counter(words)

# Save word frequencies to a file
with open('word_freqs.json', 'w', encoding='utf-8') as file:
    json.dump(word_freqs, file)
