#The Thing-A-Ma-Jig is a crazy contraption—it clanks and clunks and even thunks,
#Whether you give it lists or strings, it still does things. But how exactly does it
#work? Can you uncrack the code and find its quirks?

characters = 'taco'
output = ''
length = len(characters)
i = 0
while (i < length):
    output = output + characters[i]
    i = i + 1
length = length * -1
i = -2
while (i >= length):
    output = output + characters[i]
    i = i - 1
print(output)