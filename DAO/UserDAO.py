import psycopg2
from PyQt6.lupdate import user

from DTO.User import User
from Utils.Database import Database


class UserDAO:
    def __init__(self):
        self.connection = Database()
        self.conn = self.connection.connect()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def login(self, user):
        try:
            query = "SELECT public.user_login(%s, %s);"
            self.cursor.execute(query, (user.get_username(), user.get_password()))
            result = self.cursor.fetchone()
            was_found = result[0]
            return was_found
        except Exception as e:
            print(f"Error en la consulta de inicio de sesión: {e}")
            return False

    def insert_user(self, user):
        try:
            self.cursor.execute(
                "SELECT public.insert_user(%s, %s)",
                (user.get_username(), user.get_password())
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
            self.conn.rollback()
            return False

    def delete_user(self, username, password):
        try:
            self.cursor.execute(
                "SELECT public.delete_user(%s, %s)",
                (username, password)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al eliminar usuario: {e}")
            self.conn.rollback()
            return False

    def update_user_credentials(self, current_username, current_password, new_username, new_password):
        try:
            self.cursor.execute(
                "SELECT public.update_user_credentials(%s, %s, %s, %s)",
                (current_username, current_password, new_username, new_password)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al actualizar credenciales de usuario: {e}")
            self.conn.rollback()
            return False





