users = {}

attributes = {
'email' : 'kim@oreilly.com',
'gender': 'f',
'age': 27,
'friends': ['John', 'Josh']}
users['Kim'] = attributes
users['John'] = {'email' : 'john@abc.com','gender': 'm', 'age': 24, 'friends': ['Kim', 'Josh']}
users['Josh'] = {'email' : 'josh@wickedlysmart.com','gender': 'm', 'age': 32, 'friends': ['Kim']}
print(users)