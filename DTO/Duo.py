# Duo.py

class Duo:
    def __init__(self, id_duo, id_person1, id_person2, consider):
        self._id_duo = id_duo
        self._id_person1 = id_person1
        self._id_person2 = id_person2
        self._consider = consider

    def get_id_duo(self):
        return self._id_duo

    def set_id_duo(self, value):
        self._id_duo = value

    def get_id_person1(self):
        return self._id_person1

    def set_id_person1(self, value):
        self._id_person1 = value

    def get_id_person2(self):
        return self._id_person2

    def set_id_person2(self, value):
        self._id_person2 = value

    def get_consider(self):
        return self._consider

    def set_consider(self, value):
        self._consider = value

    def __str__(self):
        return f"Duo(id_duo={self._id_duo}, id_person1={self._id_person1}, id_person2={self._id_person2}, consider={self._consider})"
