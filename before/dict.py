d1 = {
    'key':'value',
    '屬性':'值'
}
user = {
    'name':'John',
    'mail':'john@gmail.com',
    'gender':'male'
}
# print(user.get('skill'))
# print(user['skill'])

# user['skill'] = 'Photoshop'
# user.setdefault('skill','Photoshop')

# user['name'] = 'Max'
# user.setdefault('name','Max')

# user.pop('gender')
# del user['gender']

# user.clear()
# print(user.keys())
# print(user.values())
# print(user.items())


# for item in user.values():
#     print(item)

# for key,value in user.items():
#     print(f'{key:8s}:{value:10}')
users = [
    {
        'name':'John',
        'mail':'john@gmail.com',
        'gender':'male',
        'skill': ['photoshop','python']
    },
    {
        'name':'Mary',
        'mail':'mary@gmail.com',
        'gender':'female',
        'skill': ['python','photoshop','HTML']
    }
]
# for data in users:
#     # print(data.items())
#     for k,v in data.items():
#         print(f'{k:10}:{v}')
#     print('-----------------------------------------')

# for idx in range(0,len(users)):
#     for k,v in users[idx].items():
#         print(f'{k:10}:{v}')

# print(users[0]['gender'])
# print(users[1]['name'])
# print(users[1]['mail'])
# print(users[1]['gender'])
# print(users[1]['skill'][0])
# print(users[1]['skill'][1])
# print(users[1]['skill'][2])

user2 = {
    'name':'Mary',
    'skill':'Photoshop',
    'age': 30
}
user3 = {
    'active': True
}
# user.update(user2)
user = {**user,**user2,**user3}
print(user)
