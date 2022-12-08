import geopy



def geopy_test():
    address = input('Podaj adress: ')
    if address == '':
        address = 'Mireckiego 29, 42-200 Częstochowa'
    geolocator = geopy.Nominatim(user_agent='Michal-Rak')
    address_code = geolocator.geocode(address)
    print(address_code)
    print(f'GPS: {address_code.latitude}, {address_code.longitude}')


if __name__ == '__main__':
    geopy_test()
