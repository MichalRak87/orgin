from dataclasses import dataclass

@dataclass
class Player:
    imie: str
    nazwisko: str
    wiek: int

    def __str__(self):
        return f'Imie: {self.imie}, Nazwisko: {self.nazwisko}, Wiek: {self.wiek}'

mik = Player('Michal', 'Rak', 35)


class Player2:
    liczba = 12
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def __str__(self):
        return f'Imie: {self.imie}, Nazwisko: {self.nazwisko}, Wiek: {self.wiek}'

raq = Player2('Pawel', 'Rak', 36)



class Players:
    def __init__(self, players = None):
        if players is None:
            players = []
        self.players = players

    def add_player(self, name):
        self.players.append(name)
        return self.players
    def show_list(self):
        if len(self.players) == False:
            print('Lista jest pusta')
        else:
            print('Number of players:', len(plyr_list.players))
            for number, player in enumerate(self.players):
                print(number+1,':',player)
    def del_player(self,name):
        if name in self.players:
            self.players.remove(name)




kuba = Player('Kuba', 'Rak', 26)

plyr_list = Players()
plyr_list.show_list()
print('-'*40)
plyr_list.add_player(mik)
plyr_list.add_player(raq)
plyr_list.show_list()
print('-'*40)
plyr_list.add_player(kuba)
plyr_list.show_list()

print('-'*40)
jan = Player('Jan', 'Kowalski', 20)


plyr_list.add_player(jan)
plyr_list.show_list()

plyr_list.del_player(raq)
plyr_list.show_list()
