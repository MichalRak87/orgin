def get_positiv_number():
    number = int(input('Prosze o dodatnia liczbe: '))
    if number > 0:
        return number
    else:
        print(f'{number} nie jest liczba dodatnia')
        return False


while liczba := get_positiv_number():
    print(f'Brawo {liczba} jest liczba dodatnia')