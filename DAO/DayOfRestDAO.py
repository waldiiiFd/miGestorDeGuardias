from Utils.Database import Database


class DayOfRestDAO:
    def __init__(self):
        self.connection = Database()
        self.conn = self.connection.connect()
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.conn.close()

    def insert_dayofrest(self, dayofrest):
        try:
            self.cursor.execute(
                "SELECT public.insert_dayofrest(%s)",
                (dayofrest.get_rest_day_month_year(),)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al insertar día no laborable: {e}")
            self.conn.rollback()
            return False

    def insert_daysofrest_in_interval(self, start_date, end_date):
        try:
            self.cursor.execute(
                "SELECT public.insert_daysofrest_in_interval(%s, %s)",
                (start_date, end_date)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al insertar días de descanso en intervalo: {e}")
            self.conn.rollback()
            return False

    def delete_daysofrest_in_interval(self, start_date, end_date):
        try:
            self.cursor.execute(
                "SELECT public.delete_daysofrest_in_interval(%s, %s)",
                (start_date, end_date)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al eliminar días de descanso en intervalo: {e}")
            self.conn.rollback()
            return False

    def delete_dayofrest(self, dayofrest):
        try:
            self.cursor.execute(
                "SELECT public.delete_dayofrest(%s)",
                (dayofrest.get_rest_day_month_year(),)
            )
            result = self.cursor.fetchone()[0]
            if result:
                self.conn.commit()
                return True
            else:
                return False
        except Exception as e:
            print(f"Error al eliminar día no laborable: {e}")
            self.conn.rollback()
            return False

    def get_dayofrestinformation_byyear(self, year_param):
        try:
            self.cursor.execute(
                "SELECT * FROM public.get_dayofrestinformation_byyear(%s)",
                (year_param,)
            )
            dayofrest_info = self.cursor.fetchall()
            return dayofrest_info
        except Exception as e:
            print(f"Error al obtener la información de días no laborables por año: {e}")
            return None


    ######

    def is_rest_day(self, date):
        try:
            self.cursor.execute(
                "SELECT count_rest_days(%s)",
                (date,)
            )
            count = self.cursor.fetchone()[0]
            return count > 0
        except Exception as e:
            print(f"Error al verificar si la fecha es un día de descanso: {e}")
            return False
