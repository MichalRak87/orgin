print('Simanko')
print('Jak sie masz')

imie = 'Michal'
nazwisko = 'Rak'

print(f'Witaj {imie} {nazwisko}')

szansa = 3

for _ in range(szansa):
    print(f'Masz {szansa} szanse\n')
    if imie == 'Michal' and nazwisko == 'Rak':
        haslo = input('Podaj haslo: ')
        if haslo == 'mikmik':
            print('Masz dostep admina')
            dostep = True
            break
        else:
            print('Podales zle haslo')
            szansa -= 1
            dostep = False

if dostep:
    print('Brawo Ty')
else:
    print('Konto zablokowane')