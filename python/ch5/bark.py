print('Get those dogs ready')

def bark(name, weight): #parameters
    if weight > 20:
        print(name, 'says WOOF WOOF')
    else:
        print(name, 'says woof woof')

bark('Codie', 40) #arguments
bark('Sparky', 9)
bark('jackson', 12)
bark('Fido', 65)
bark('Barnaby', -1)
print("Okay, we're all done")
