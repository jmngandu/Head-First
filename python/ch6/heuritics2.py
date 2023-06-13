
def compute_readability(text):
    total_words = 0
    total_sentences = 0
    total_syllables = 0
    score = 0
    words = text.split()
    total_words = len(words)
    total_sentences = count_sentences(text)
    total_syllables = count_syllables(words)
score = (206.835 - 1.015 * (total_words / total_sentences)
                    - 84.6 * (total_syllables / total_words))

print(total_sentences, 'sentences')
print(total_syllables, 'syllables')
print(score, 'reading ease score')