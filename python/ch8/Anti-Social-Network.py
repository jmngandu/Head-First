my_dictionary = {}
my_dictionary['jenny'] = '126-4344'
my_dictionary['james'] = '600-7004'
my_dictionary['paul'] = '555-1201'
my_dictionary['david'] = '321-6617'
my_dictionary['jamie'] = '771-0091'
del my_dictionary['jamie']

phone_number = my_dictionary['jenny']
print('jennis number is ',phone_number)
if 'jenny' in my_dictionary:
    print('found her ', my_dictionary['jenny'])
else:
    print('I need to get her number')

for key in my_dictionary:
    print(key, ":", my_dictionary[key])

harry = {'firstname': 'Harry', 'lastname': 'Potter', 'house': 'Gryffindor', 'friends': ['Ron', 'Hermione'], 'born': 1980}
print(my_dictionary)