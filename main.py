
# dict = {
#     1: 'Alica',
#     2: 'Bail', 
#     3: 'Griha',

# }

# dict.clear()

# dict['email'] = 'kishkovarv@gmail.com'
# dict['name'] = 'Vladislav'
# dict['lastname'] = 'Kishkovar'

# for key, vlaues in dict.items():
#     print(f'{key} -_- {vlaues}')

names = {
    'name': 'Vlad',
    'last_name': 'Kishkovar',
    'email': 'kishkovarv@gmail.com'
}

def strings(s):
    list = ''
    for i in s:
        list += f' {i}'
    list = list[1:]
    return list
# print(strings("hellokishkovar"))

tuple = 1, 2, 4
g = 1, 2, True, True
tuple += g
tuple = list(tuple)

# for i in range(2):
#     list = tuple.pop()

tuple.reverse()

def fnc():
    list = []
    for i in range(1, 6):
        list.append(i)
    p = list.pop()
    return p


list = [1,2,3,4,5,True]
list = set(list)
# set = {1, 2, 3, 4, 5, 5}

users = ['Ivan', 'Olga', 'Danil', 'Vlad', 'Oleg', 'Danil']

def sum_num(l, t):
    total = 0
    for i in l:
        s = t - i
        if s in l:
            total = s + i
    print(total)
sum_num([2, 7, 11, 15], 9)