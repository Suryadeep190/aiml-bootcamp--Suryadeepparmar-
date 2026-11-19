import string
from collections import Counter

with open("sample.txt", "r", encoding="utf-8") as file:
    text = file.read()




text = text.lower()

text = text.translate(str.maketrans("", "", string.punctuation))

words = text.split()



word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("\n--- Traditional Dictionary Approach ---")

for word, count in word_count.items():
    print(f"{word}: {count}")



counter_count = Counter(words)

print("\n--- Counter Approach ---")

for word, count in counter_count.items():
    print(f"{word}: {count}")



print("\n--- Comparison ---")

print("Dictionary total words:", sum(word_count.values()))
print("Counter total words:", counter_count.total())

print("Both approaches give the same result:",
      word_count == counter_count)



print("\n--- Top 10 Most Common Words ---")

for word, count in counter_count.most_common(10):
    print(f"{word}: {count}")



stopwords = {
    "the", "a", "an", "and", "is", "are", "for",
    "to", "of", "in", "it", "with", "about",
    "because", "their", "like", "not"
}

filtered_words = [
    word for word in words
    if word not in stopwords
]


filtered_counter = Counter(filtered_words)

print("\n--- Top 10 Words After Removing Stopwords ---")

for word, count in filtered_counter.most_common(10):
    print(f"{word}: {count}")