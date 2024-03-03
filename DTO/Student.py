# Student.py

from DTO.Person import Person

class Student(Person):
    def __init__(self, id_number, full_name, sex, current_state, type_person, group):
        super().__init__(id_number, full_name, sex, current_state, type_person)
        self._group = group

    def __str__(self):
        return super().__str__() + f", Group: {self._group}"

    # Getter y setter específico para el atributo 'group'
    def get_group(self):
        return self._group

    def set_group(self, group):
        self._group = group
