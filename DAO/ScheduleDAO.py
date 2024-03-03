from Utils.Database import Database


class ScheduleDAO:
    def __init__(self):
        self.connection = Database()
        self.conn = self.connection.connect()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def insert_schedule(self, day_of_week_input, begin_time_input, end_time_input, rol_input, sex_input=None):
        try:
            if sex_input is not None:
                self.cursor.execute(
                    "SELECT public.insert_schedule(%s, %s, %s, %s, %s)",
                    (day_of_week_input, begin_time_input, end_time_input, rol_input, sex_input)
                )
            else:
                self.cursor.execute(
                    "SELECT public.insert_schedule(%s, %s, %s, %s)",
                    (day_of_week_input, begin_time_input, end_time_input, rol_input)
                )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al insertar el horario: {e}")
            self.conn.rollback()
            return False

    def delete_schedule(self, day_of_week_input, begin_time_input, end_time_input):
        try:
            self.cursor.execute(
                "SELECT public.delete_schedule(%s, %s, %s)",
                (day_of_week_input, begin_time_input, end_time_input)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al eliminar el horario: {e}")
            self.conn.rollback()
            return False

    def get_all_schedules(self):
        try:
            self.cursor.execute("SELECT * FROM public.get_all_schedule()")
            schedules = self.cursor.fetchall()
            return schedules
        except Exception as e:
            print(f"Error al obtener todos los horarios: {e}")

            return None

    def get_schedule_for_person(self, rol, sex=None):
        try:
            if sex is None:
                self.cursor.execute(
                    "SELECT * FROM get_schedule_for_person(%s)",
                    (rol,)
                )
            else:
                self.cursor.execute(
                    "SELECT * FROM get_schedule_for_person(%s, %s)",
                    (rol, sex)
                )
            schedule_info = self.cursor.fetchall()
            if schedule_info:
                return schedule_info
            else:
                print("No se encontró un horario para el rol y sexo especificados.")
                return None
        except Exception as e:
            print(f"Error al obtener el horario para el rol y sexo especificados: {e}")
            return None


