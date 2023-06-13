#Finding syllables is a messy business because the English language is messy. For instance, why does “walked” have
#one syllable while “loaded” is two? English is full of such inconsistencies.
#For problems like this we don’t write algorithms, we write heuristics. A heuristic is a lot like an algorithm, only it’s
#not a 100% solution. It might, for instance, solve a problem with a good answer, but not necessarily a perfect
#answer.
def count_syllables(words):
    count = 0
for word in words:
    word_count = count_syllables_in_word(word)
    count = count + word_count
return count
def count_syllables_in_word(word):
    count = 0
    return count