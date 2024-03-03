from Utils.Database import Database


class StudentDAO:
    def __init__(self):
        connection = Database()
        self.conn = connection.connect()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def insert_student(self, student):
        try:
            self.cursor.execute(
                "SELECT public.insert_student(%s, %s, %s, %s, %s)",
                (student.get_id_number(), student.get_full_name(), student.get_current_state(), student.get_group(),
                 student.get_sex())
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al insertar estudiante: {e}")
            self.conn.rollback()
            return False

    def get_all_students(self):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_all_students()"
            )
            students = self.cursor.fetchall()
            return students
        except Exception as e:
            print(f"Error al obtener todos los estudiantes: {e}")
            return None

    def update_student_group(self, student):
        try:
            self.cursor.execute(
                "SELECT public.update_student_group(%s, %s)",
                (student.get_id_number(), student.get_group())
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al actualizar estudiante: {e}")
            self.conn.rollback()
            return False









