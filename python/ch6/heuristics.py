#Finding syllables is a messy business because the English language is messy. For instance, why does “walked” have
#one syllable while “loaded” is two? English is full of such inconsistencies.
#For problems like this we don’t write algorithms, we write heuristics. A heuristic is a lot like an algorithm, only it’s
#not a 100% solution. It might, for instance, solve a problem with a good answer, but not necessarily a perfect
#answer.
import ch1text
def count_syllables(words):
    count = 0
    for word in words:
        word_count = count_syllables_in_word(word)
        count = count + word_count
    return count
def count_syllables_in_word(word):
    count = 0
    endings = '.,;!?:'
    last_char = word[-1]
    if last_char in endings:
        processed_word = word[0:-1]
    else:
        processed_word = word
    if len(processed_word) <= 3:
        return 1
    if processed_word[-1] in 'eE':
        processed_word = processed_word[0:-1]
    vowels = "aeiouAEIOU"
    prev_char_was_vowel = False
    for char in processed_word:
        if char in vowels:
            if not prev_char_was_vowel:
                count = count + 1
            prev_char_was_vowel = True
        else:
            prev_char_was_vowel = False
    if processed_word[-1] in 'yY':
        count = count + 1
    return count

    print(total_words, 'words')
print(total_sentences, 'sentences')
print(total_syllables, 'syllables')
print(score, 'reading ease score')

    