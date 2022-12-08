from math import ceil


class InvalidSemester(Exception):
    pass


class Student:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.semester = 1

    def go_up(self,semester_number=1):
        self.semester += semester_number

    def go_down(self,semester_number=1):
        if self.semester <= 1:
            raise InvalidSemester
        else:
            self.semester -= semester_number

    def hello(self):
        return f'Imie: {self.first_name}\nNazwisko: {self.last_name}\nSemestr: {self.semester}\nRok: {self.year}'

    @property
    def year(self):
        return ceil(self.semester / 2)


try:
    janek = Student('Janusz','Nowak')
    ania = Student('Ania','Rak')
    janek.go_up(2)
    ania.go_up(3)
except InvalidSemester as message:
    print(f'Nie mozesz odjasc semestru')
else:
    print(janek.hello())
    print()
    print(ania.hello())

