# Schedule.py

class Schedule:
    def __init__(self, id_schedule, day_of_week, begin_time, end_time, rol, sex):
        self._id_schedule = id_schedule
        self._day_of_week = day_of_week
        self._begin_time = begin_time
        self._end_time = end_time
        self._rol = rol
        self._sex = sex

    @property
    def id_schedule(self):
        return self._id_schedule

    @id_schedule.setter
    def id_schedule(self, value):
        self._id_schedule = value

    @property
    def day_of_week(self):
        return self._day_of_week

    @day_of_week.setter
    def day_of_week(self, value):
        self._day_of_week = value

    @property
    def begin_time(self):
        return self._begin_time

    @begin_time.setter
    def begin_time(self, value):
        self._begin_time = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        self._end_time = value

    @property
    def rol(self):
        return self._rol

    @rol.setter
    def rol(self, value):
        self._rol = value

    @property
    def sex(self):
        return self._sex

    @sex.setter
    def sex(self, value):
        self._sex = value
