users = {'Kim' : 'kim@oreilly.com',
        'John': 'john@abc.com',
        'Josh': 'josh@wickedlysmart.com'}
users['Avary'] = 'avary@gmail.com'
del users['John']
if 'Josh' in users:
    print("Josh's email address is:", users['Josh'])