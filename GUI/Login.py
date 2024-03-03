from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMessageBox
from DAO.UserDAO import UserDAO
from DTO.User import User
from GUI.Main import Main


class Login:
    def __init__(self):
        self.main = None
        self.login = uic.loadUi("GUI/Login.ui")
        self.initGUI()
        self.login.lblMensaje.setText("")
        self.login.show()



    def initGUI(self):
        self.login.btnAcceder.clicked.connect(self.insert_data)

    def insert_data(self):
        if len(self.login.txtUsuario.text()) < 2:
            self.login.lblMensaje.setText("Ingrese un usuario válido!")
            self.login.txtUsuario.setText("")
            self.login.txtClave.setText("")
            self.login.txtUsuario.setFocus()
        elif len(self.login.txtClave.text()) < 2:
            self.login.lblMensaje.setText("Ingrese una contraseña válida!")
            self.login.txtUsuario.setText("")
            self.login.txtClave.setText("")
            self.login.txtClave.setFocus()
        else:
            self.login.lblMensaje.setText("")
            user = User(username=self.login.txtUsuario.text(), password=self.login.txtClave.text())
            user_dao = UserDAO()
            result = user_dao.login(user)
            if result:
                    self.main=Main()
                    self.login.hide()
            else:
                self.login.lblMensaje.setText("Usuario no encontrado!")
                self.login.txtUsuario.setText("")
                self.login.txtClave.setText("")
