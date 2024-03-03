# Person.py

class Person:
    def __init__(self, id_number, full_name, sex, current_state, type_person, id_person=None):
        self._id_person = id_person
        self._id_number = id_number
        self._full_name = full_name
        self._sex = sex
        self._current_state = current_state
        self._type_person = type_person

    def __str__(self):
        return f"ID: {self._id_person}, ID Number: {self._id_number}, Full Name: {self._full_name}, Sex: {self._sex}, Current State: {self._current_state}, Type: {self._type_person}"

    # Getters y setters
    def get_id_person(self):
        return self._id_person

    def set_id_person(self, id_person):
        self._id_person = id_person

    def get_id_number(self):
        return self._id_number

    def set_id_number(self, id_number):
        self._id_number = id_number

    def get_full_name(self):
        return self._full_name

    def set_full_name(self, full_name):
        self._full_name = full_name

    def get_sex(self):
        return self._sex

    def set_sex(self, sex):
        self._sex = sex

    def get_current_state(self):
        return self._current_state

    def set_current_state(self, current_state):
        self._current_state = current_state

    def get_type_person(self):
        return self._type_person

    def set_type_person(self, type_person):
        self._type_person = type_person
