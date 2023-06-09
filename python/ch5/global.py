greeting = 'Greetings'
def greet(name, message):
    global greeting
    greeting = 'Hi'
    print(greeting, name + '.', message)
greet('june', 'See you soon!')