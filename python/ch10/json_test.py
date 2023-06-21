import json
#And here’s a string containing JSON Note, to Python, this is just a string with some text it.
json_string = '{"first": "james", "last": "Ngandu", "prefix": "Dr."}'
#So let’s call json.loads on the string, and assign the resulting dictionary to the variable name.
name = json.loads(json_string)
#And finally let’s use the Python dictionary to access the first and last name attributes along with the prefix attribute.
print(name['prefix'], name['first'], name['last'])
