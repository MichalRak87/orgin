class Student:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def przedstaw_sie(self):
        return f'{self.first_name},{self.last_name}'



janek = Student(first_name = 'Janusz', last_name = 'Nowak')
malgosia = Student('Malgosia', 'Kowalska')


print(janek.przedstaw_sie())
print(malgosia.przedstaw_sie())


