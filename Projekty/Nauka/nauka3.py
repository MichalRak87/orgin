def uppercase(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return wrapper



@uppercase
def hello(name = ''):
    return f'Hello {name}'


lista ={'login':'password','michal':'rak','jan':'nowak'}
for i in lista:
    print(hello(i))
    print(hello(lista[i]))
    print()


