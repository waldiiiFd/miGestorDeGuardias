from Utils.Database import Database


class DuoDAO:
    def __init__(self):
        self.connection = Database()
        self.conn = self.connection.connect()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def delete_duo(self, id_number1, id_number2):
        try:
            self.cursor.execute(
                "SELECT public.delete_duo(%s, %s)",
                (id_number1, id_number2)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True  # El dúo fue eliminado exitosamente
            else:
                return False  # No se encontró el dúo para eliminar
        except Exception as e:
            print(f"Error al eliminar el dúo: {e}")
            self.conn.rollback()
            return False

    def insert_duo(self, id_number1, id_number2):
        try:
            self.cursor.execute(
                "SELECT public.insert_duo(%s, %s)",
                (id_number1, id_number2)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True  # El dúo fue insertado exitosamente
            else:
                return False  # No se pudo insertar el dúo
        except Exception as e:
            print(f"Error al insertar el dúo: {e}")
            self.conn.rollback()
            return False

    def update_duo_consider_by_current_state(self):
        try:
            self.cursor.execute(
                "SELECT public.update_duo_considerbycurrentstate()"
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True  # Se actualizó al menos una fila en la tabla Duo
            else:
                return False  # No se actualizó ninguna fila en la tabla Duo
        except Exception as e:
            print(f"Error al actualizar el parámetro consider en la tabla Duo: {e}")
            self.conn.rollback()
            return False

    def update_duo_consider_by_id(self, id_number1, id_number2, new_consider):
        try:
            self.cursor.execute(
                "SELECT public.update_duo_considerbyid(%s, %s, %s)",
                (id_number1, id_number2, new_consider)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True  # Se actualizó al menos una fila en la tabla Duo
            else:
                return False  # No se actualizó ninguna fila en la tabla Duo
        except Exception as e:
            print(f"Error al actualizar el parámetro consider en la tabla Duo: {e}")
            self.conn.rollback()
            return False

    def get_all_duoinformation(self):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_all_duoinformation()"
            )
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al obtener la información de los dúos: {e}")
            return None


