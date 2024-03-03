from PyQt6.QtWidgets import QApplication

from GUI.Login import Login


class Manager:

    def __init__(self):
        self.app = QApplication([])
        self.login = Login()
        self.app.exec()
