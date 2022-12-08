def uppercase(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return wrapper


def repeat(times):
    def wrapper(func):
        def inner_wrapper(*args,**kwargs):
            r = []
            for _ in range(times):
                r.append(func(*args,**kwargs))
            return r
        return inner_wrapper
    return wrapper


def title(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).title()
    return wrapper


def show(func):
    lista = func()
    for i, v in enumerate(lista):
        print(i+1, v)


@show
@repeat(int(input('Ile razy powtorzyc: ')))
@uppercase
def hello(name=input('Podaj imie: ')):
    return f'hello {name}'

