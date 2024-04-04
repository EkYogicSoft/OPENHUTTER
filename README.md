# OPENHUTTER
OPENHUTTER Project. I place where I dump my unimplemented project hutter ideas to find colaborators

---

For the task you've outlined, let's start with a Python script that will open the enwik6 file, split it by spaces to form a basic dictionary of words and their frequencies, and then explore a method to estimate the complexity of reordering these words based on frequency.

### Step 1: Creating the Dictionary and Saving Frequencies

```python
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
```

### Step 2: Estimating the Number of Iterations for Ordering

The next step involves estimating the number of iterations it would take to order these words. This could get complex and may involve combinatorics if we were to calculate exact permutations. However, for a simplified estimation or approach to compression, we could consider the frequency of each word as a basic measure of its "distance" from an arbitrary ordering point (like the most frequent word).

### Theoretical Discussion on Compression Technique

The proposed statistical approach for compression—saving the index of the current word as the distance from the most frequent word—suggests a method to encode text based on the relative positions of words in a frequency-sorted list. While innovative, accurately decompressing this information to retrieve the original text depends on the maintenance of consistent word order and frequency distribution. The effectiveness of this technique would vary significantly with the nature of the text and might not universally apply as efficiently as traditional compression methods.

Calculating the exact number of iterations for a set of items to be ordered or representing this as a permutation number introduces a level of mathematical complexity. In practice, such methods need to balance computational efficiency with the accuracy and utility of the compressed representation. Exploring these concepts could lead to interesting insights into data compression, although practical application might require significant computational resources or simplifications to be feasible.

+++




1. **Spawning Words by Frequency:**
   - Use the word frequencies you've obtained to generate a text where each word appears as often as its frequency indicates. This creates a "decompressed" version of your text, essentially reversing the compression to its original or an expanded form.

2. **K-th Permutation Method for Original Data Representation:**
   - The idea of using the k-th permutation method to represent your data is intriguing. This would involve mapping your decompressed text back to a number that represents its position in the permutation of all possible texts given the dictionary. The challenge here lies in the computational complexity of finding this permutation number for large datasets.

3. **Distance to Most Occurring Character:**
   - Assigning a number based on the distance to the most occurring word is a compression technique that mirrors concepts used in Huffman coding. This approach could potentially reduce the space needed to represent each word based on its frequency and relative position in the text.

**Implementation Notes:**
- For the first step, consider Python dictionaries and loops to iterate through the frequencies and spawn the text.
- For the second step, research efficient algorithms for finding k-th permutations, keeping in mind the scalability for large text.
- For the third step, dynamically maintain a list or heap of word frequencies as you process the text, allowing you to encode words based on their frequency at any point in the document.

**To-Do and Considerations:**
- Explore libraries or algorithms that can efficiently handle large permutations.
- Consider the memory implications of handling large datasets, especially when decompressing or finding permutations.
- Research compression techniques and algorithms for insights on encoding based on frequency and relative position.

This PoC combines several advanced concepts in data compression and algorithm design. Engaging with experts in mathematics, computer science, and data compression could provide further insights and help refine your approach.

@@@

write to sombrero.azul37 at the mailing of proton.


