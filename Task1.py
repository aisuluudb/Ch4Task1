class Student():
    pass

    def __init__(self, name, lastname, department, year_of_entrance):
        self.name = name
        self.lastname = lastname
        self.department = department
        self.year_of_entrance = year_of_entrance

    def get_student_info(self):
        print(f'{self.name} {self.lastname} поступила в {self.year_of_entrance} году на факультет {self.department}')

stud = Student('Alisa', 'Kopeva', 'Sociology', 2011)
stud.get_student_info()