# DTO.py

class DayOfRest:
    def __init__(self, rest_day_month_year, id=None):
        self._id = id
        self._rest_day_month_year = rest_day_month_year

    def __str__(self):
        return f"ID: {self._id}, Rest Day Month Year: {self._rest_day_month_year}"

    # Getter y setter para 'id'
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    # Getter y setter para 'restDayMonthYear'
    def get_rest_day_month_year(self):
        return self._rest_day_month_year

    def set_rest_day_month_year(self, rest_day_month_year):
        self._rest_day_month_year = rest_day_month_year


