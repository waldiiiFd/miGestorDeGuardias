from Utils.Database import Database


class PersonDAO:
    def __init__(self):
        self.connection = Database()
        self.conn = self.connection.connect()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def insert_worker(self, person):
        try:
            self.cursor.execute(
                "SELECT public.insert_worker(%s, %s, %s, %s)",
                (person.get_id_number(), person.get_full_name(), person.get_current_state(), person.get_sex())
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al insertar trabajador: {e}")
            self.conn.rollback()
            return False

    def delete_person(self, p_id_number):
        try:
            self.cursor.execute(
                "SELECT public.delete_person(%s)",
                (p_id_number,)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al eliminar la persona: {e}")
            self.conn.rollback()
            return False

    def update_person_state(self, p_id_number, p_new_state):
        try:
            self.cursor.execute(
                "SELECT public.update_person_state(%s, %s)",
                (p_id_number, p_new_state)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al actualizar el estado de la persona: {e}")
            self.conn.rollback()
            return False

    def get_all_workers(self):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_all_workers()"
            )
            workers = self.cursor.fetchall()
            return workers
        except Exception as e:
            print(f"Error al obtener todos los trabajadores: {e}")
            return None

    def get_person_information(self, p_id_number):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_person_information(%s)",
                (p_id_number,)
            )
            person_info = self.cursor.fetchone()
            return person_info
        except Exception as e:
            print(f"Error al obtener la información de la persona: {e}")
            return None



