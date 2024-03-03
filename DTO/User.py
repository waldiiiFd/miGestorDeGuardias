# User.py

class User:
    def __init__(self, id=None, username=None, password=None, last_login=None):
        self._id = id
        self._username = username
        self._password = password
        self._last_login = last_login

    # Getters
    def get_id(self):
        return self._id

    def get_username(self):
        return self._username

    def get_password(self):
        return self._password

    def get_last_login(self):
        return self._last_login

    # Setters
    def set_id(self, id):
        self._id = id

    def set_username(self, username):
        self._username = username

    def set_password(self, password):
        self._password = password

    def set_last_login(self, last_login):
        self._last_login = last_login


