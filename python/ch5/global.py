greeting = 'Greetings'
def greet(name, message):
    global greeting
    print(greeting, name + '.', message)
greet('june', 'See you soon!')