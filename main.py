def palindrom(s):
    if s == s[::-1]:
        return True
    return False

def types(j):
    # Строки являются не изменяемым типом для того безопасности данных.
    if type(j) == int:
        return f'неизменяемые тип'
    elif type(j) == str:
        return f'неизменяемые тип'
    elif type(j) == tuple:
        return f'неизменяемые тип'
    elif type(j) == float:
        return f'неизменяемые тип'
    elif type(j) == frozenset:
        return f'неизменяемые тип'
    elif type(j) == bytes:
        return f'неизменяемые тип'
    else:
        return f'изменяемый тип'
    
s = 'hello'