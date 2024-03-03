from datetime import timedelta

from DAO.DayOfRestDAO import DayOfRestDAO
from DAO.ScheduleDAO import ScheduleDAO
from Utils.Database import Database


class GuardshiftDAO:
    def __init__(self):
        self.connection = Database()
        self.conn = self.connection.connect()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def get_previous_guard_shifts(self):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_previous_guard_shifts()"
            )
            guard_shifts_info = self.cursor.fetchall()
            return guard_shifts_info
        except Exception as e:
            print(f"Error al obtener los turnos de guardia anteriores: {e}")
            return None

    def delete_guard_shift(self, p_day_month_year, p_begin_time, p_end_time):
        try:
            self.cursor.execute(
                "SELECT public.delete_guard_shift(%s, %s, %s)",
                (p_day_month_year, p_begin_time, p_end_time)
            )
            result = self.cursor.fetchone()[0]
            self.conn.commit()
            return result
        except Exception as e:
            print(f"Error al eliminar turno de guardia: {e}")
            self.conn.rollback()
            return False

    def get_guard_shift_count(self, p_id_number):
        try:
            self.cursor.execute(
                "SELECT public.get_guard_shift_count(%s)",
                (p_id_number,)
            )
            guard_shift_count = self.cursor.fetchone()[0]
            return guard_shift_count
        except Exception as e:
            print(f"Error al obtener el conteo de turnos de guardia: {e}")
            return None

    def get_guard_shiftsinformationbydate(self, p_daymonthyear):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_guard_shiftsinformationbydate(%s)",
                (p_daymonthyear,)
            )
            guard_shifts_info = self.cursor.fetchall()
            return guard_shifts_info
        except Exception as e:
            print(f"Error al obtener la información de los turnos de guardia por fecha: {e}")
            return None

    def get_guard_shiftsinformationbyid_number(self, p_id_number):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_guard_shiftsinformationbyid_number(%s)",
                (p_id_number,)
            )
            guard_shifts_info = self.cursor.fetchall()
            return guard_shifts_info
        except Exception as e:
            print(f"Error al obtener la información de los turnos de guardia por ID de persona: {e}")
            return None

    def get_last_guard_shift(self, p_id_number):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_last_guard_shift(%s)",
                (p_id_number,)
            )
            last_guard_shift_info = self.cursor.fetchone()
            return last_guard_shift_info
        except Exception as e:
            print(f"Error al obtener la última información del turno de guardia: {e}")
            return None

    def get_upcoming_guard_shifts(self):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_upcoming_guard_shifts()"
            )
            upcoming_guard_shifts_info = self.cursor.fetchall()
            return upcoming_guard_shifts_info
        except Exception as e:
            print(f"Error al obtener los próximos turnos de guardia: {e}")
            return None

    def get_missing_shiftsStudentM(self):
        try:
            self.cursor.execute(
                "SELECT * FROM get_missing_shiftsStudentM()"
            )
            missing_shifts_info = self.cursor.fetchall()
            return missing_shifts_info
        except Exception as e:
            print(f"Error al obtener los turnos de guardia faltantes: {e}")
            return None
    def get_missing_shiftsStudentF(self):
        try:
            self.cursor.execute(
                "SELECT * FROM get_missing_shiftsstudentf()"
            )
            missing_shifts_info = self.cursor.fetchall()
            return missing_shifts_info
        except Exception as e:
            print(f"Error al obtener los turnos de guardia faltantes: {e}")
            return None


    def get_missing_shiftsWorker(self):
        try:
            self.cursor.execute(
                "SELECT * FROM get_missing_shiftsWorker()"
            )
            missing_shifts_info = self.cursor.fetchall()
            return missing_shifts_info
        except Exception as e:
            print(f"Error al obtener los turnos de guardia faltantes: {e}")
            return None

    def insert_guard_shift(self, p_day_month_year, p_begin_time, p_end_time, p_id_number1, p_id_number2):
        try:
            self.cursor.execute(
                "SELECT public.insert_guard_shift(%s, %s, %s, %s, %s)",
                (p_day_month_year, p_begin_time, p_end_time, p_id_number1, p_id_number2)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al insertar turno de guardia: {e}")
            self.conn.rollback()
            return False

    def update_guard_shift_assistance(self, p_day_month_year, p_begin_time, p_end_time, p_id_number1, p_id_number2,
                                      p_assistance1, p_assistance2):
        try:
            self.cursor.execute(
                "SELECT public.update_guard_shift_assistance(%s, %s, %s, %s, %s, %s, %s)",
                (p_day_month_year, p_begin_time, p_end_time, p_id_number1, p_id_number2, p_assistance1, p_assistance2)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al actualizar la asistencia del turno de guardia: {e}")
            self.conn.rollback()
            return False

    def update_guard_shift_changeparticipants(self, p_day, p_begin_time, p_end_time, p_id_number, p_daychange, p_begin_timechange, p_end_timechange, p_id_numberchange):
        try:
            self.cursor.execute(
                "SELECT public.update_guard_shift_changeparticipants(%s, %s, %s, %s, %s, %s, %s, %s)",
                (p_day, p_begin_time, p_end_time, p_id_number, p_daychange, p_begin_timechange, p_end_timechange, p_id_numberchange)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al actualizar los participantes del turno de guardia: {e}")
            self.conn.rollback()
            return False

    def workers_without_guard_last_month(self):
        try:
            self.cursor.execute(
                "SELECT * FROM public.workers_without_guard_last_month()"
            )
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al llamar a la función: {e}")
            return []

    def get_duoid(self, p_id_number):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_duoid(%s)",
                (p_id_number,)
            )
            result = self.cursor.fetchall()
            return result
        except Exception as e:
            print(f"Error al llamar a la función: {e}")
            return None

    def students_without_guard_last_month3(self, p_sex):
        try:
            self.cursor.execute(
                "SELECT * FROM public.students_without_guard_last_month3(%s)",
                (p_sex,)
            )
            result = self.cursor.fetchall()
            return result
        except Exception as e:
               print(f"Error al llamar a la función: {e}")
               return None






