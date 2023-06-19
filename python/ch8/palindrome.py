def the_palindrome(word):
    if len(word) <= 1:
        return True
    else:
        if word[0] == word[-1]:
            return the_palindrome(word[0:-1])
        else:
            return False
words = ('a', 'tacocat', 'james', 'ada', 'kenya')
for word in words:
    print(word, the_palindrome(word))
