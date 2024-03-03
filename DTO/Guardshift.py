from datetime import timedelta, datetime



from DAO.DayOfRestDAO import DayOfRestDAO
from DAO.PersonDAO import PersonDAO
from DAO.ScheduleDAO import ScheduleDAO
from DAO.GuardshiftDAO import GuardshiftDAO


class GuardShift:
    def __init__(self, id_guard=None, dayMonthYear="", assistance_person1=False, id_person2="",
                 assistance_person2=False, id_person1="", begin_time="", end_time=""):
        self._id_guard = id_guard
        self._dayMonthYear = dayMonthYear
        self._assistance_person1 = assistance_person1
        self._id_person2 = id_person2
        self._assistance_person2 = assistance_person2
        self._id_person1 = id_person1
        self._begin_time = begin_time
        self._end_time = end_time

    def get_id_guard(self):
        return self._id_guard

    def set_id_guard(self, id_guard):
        self._id_guard = id_guard

    # Getter y Setter para dayMonthYear
    def get_dayMonthYear(self):
        return self._dayMonthYear

    def set_dayMonthYear(self, dayMonthYear):
        self._dayMonthYear = dayMonthYear

    # Getter y Setter para assistance_person1
    def get_assistance_person1(self):
        return self._assistance_person1

    def set_assistance_person1(self, assistance_person1):
        self._assistance_person1 = assistance_person1

    # Getter y Setter para id_person2
    def get_id_person2(self):
        return self._id_person2

    def set_id_person2(self, id_person2):
        self._id_person2 = id_person2

    # Getter y Setter para assistance_person2
    def get_assistance_person2(self):
        return self._assistance_person2

    def set_assistance_person2(self, assistance_person2):
        self._assistance_person2 = assistance_person2

    # Getter y Setter para id_person1
    def get_id_person1(self):
        return self._id_person1

    def set_id_person1(self, id_person1):
        self._id_person1 = id_person1

    # Getter y Setter para begin_time
    def get_begin_time(self):
        return self._begin_time

    def set_begin_time(self, begin_time):
        self._begin_time = begin_time

    # Getter y Setter para end_time
    def get_end_time(self):
        return self._end_time

    def set_end_time(self, end_time):
        self._end_time = end_time



    def crearTurnoEstudiantesMAusentesUltimaGuardia(self, begin_date, end_date, rol, sex=None):
        current_date = begin_date
        parejas_estudiantes_ausentes = set()

        try:
            # Obtener todas las personas ausentes
            estudiantesM_ausentes = GuardshiftDAO().get_missing_shiftsStudentM()
        except Exception as e:
            print(f"Error al obtener las personas ausentes: {e}")


        for i in range(0, len(estudiantesM_ausentes), 2):
            persona1 = estudiantesM_ausentes[i][0]
            persona2 = estudiantesM_ausentes[i + 1][0] if i + 1 < len(estudiantesM_ausentes) else None

            # Verificar si hay una pareja y si no está en lista_aux
            if persona2 is not None and ((persona1, persona2) not in parejas_estudiantes_ausentes) and (
                    (persona2, persona1) not in parejas_estudiantes_ausentes):
                parejas_estudiantes_ausentes.add((persona1, persona2))  # Usando add() correctamente

        # Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
        lista_aux_iter = iter(list(parejas_estudiantes_ausentes))

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person(rol, sex)

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            try:
                                # Intentar obtener el siguiente par de personas de lista_aux
                                persona1, persona2 = next(lista_aux_iter, (None, None))
                                if persona1 is not None and persona2 is not None:
                                    guardia_dao = GuardshiftDAO()
                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                            except Exception as e:
                                print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {rol} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {rol} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)

    def crearTurnoEstudiantesFAusentesUltimaGuardia(self, begin_date, end_date, rol, sex=None):
        current_date = begin_date
        parejas_estudiantes_ausentes = set()

        try:
            # Obtener todas las personas ausentes
            estudiantesF_ausentes = GuardshiftDAO().get_missing_shiftsStudentF()
        except Exception as e:
            print(f"Error al obtener las personas ausentes: {e}")

        for i in range(0, len(estudiantesF_ausentes), 2):
            persona1 = estudiantesF_ausentes[i][0]
            persona2 = estudiantesF_ausentes[i + 1][0] if i + 1 < len(estudiantesF_ausentes) else None

            # Verificar si hay una pareja y si no está en lista_aux
            if persona2 is not None and ((persona1, persona2) not in parejas_estudiantes_ausentes) and (
                    (persona2, persona1) not in parejas_estudiantes_ausentes):
                parejas_estudiantes_ausentes.add((persona1, persona2))  # Usando add() correctamente

        # Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
        lista_aux_iter = iter(list(parejas_estudiantes_ausentes))

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person(rol, sex)

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            try:
                                # Intentar obtener el siguiente par de personas de lista_aux
                                persona1, persona2 = next(lista_aux_iter, (None, None))
                                if persona1 is not None and persona2 is not None:
                                    guardia_dao = GuardshiftDAO()
                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                            except Exception as e:
                                print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {rol} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {rol} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)

    def crearTurnoTrabajadoresAusentesUltimaGuardia(self, begin_date, end_date):
        current_date = begin_date
        parejas_trabajadores_ausentes = set()

        try:
            # Obtener todas las personas ausentes
            trabajadores_ausentes = GuardshiftDAO().get_missing_shiftsWorker()
        except Exception as e:
            print(f"Error al obtener las personas ausentes: {e}")


        for i in range(0, len(trabajadores_ausentes), 2):
            persona1 = trabajadores_ausentes[i][0]
            persona2 = trabajadores_ausentes[i + 1][0] if i + 1 < len(trabajadores_ausentes) else None

            # Verificar si hay una pareja y si no está en lista_aux
            if persona2 is not None and ((persona1, persona2) not in parejas_trabajadores_ausentes) and (
                    (persona2, persona1) not in parejas_trabajadores_ausentes):
                parejas_trabajadores_ausentes.add((persona1, persona2))  # Usando add() correctamente

        # Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
        lista_aux_iter = iter(list(parejas_trabajadores_ausentes))

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person("Trabajador")

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            try:
                                # Intentar obtener el siguiente par de personas de lista_aux
                                persona1, persona2 = next(lista_aux_iter, (None, None))
                                if persona1 is not None and persona2 is not None:
                                    guardia_dao = GuardshiftDAO()
                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                            except Exception as e:
                                print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {'Trabajador'} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {'Trabajador'} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)


    def crearTurnoPersonasAusentesUltimaGuardia(self, begin_date, end_date):
            self.crearTurnoEstudiantesFAusentesUltimaGuardia(begin_date, end_date, 'Estudiante', 'F')
            self.crearTurnoEstudiantesMAusentesUltimaGuardia(begin_date, end_date, 'Estudiante', 'M')
            self.crearTurnoTrabajadoresAusentesUltimaGuardia(begin_date, end_date, 'Trabajador')

    def crearTurnoTrabajadoresNoMesPasado(self, begin_date, end_date):

        parejasDuo = set()
        trabajadores = set()  # Inicializado como conjunto
        parejasporplanificar = set()

        try:
            trabajadores = GuardshiftDAO().workers_without_guard_last_month()  # Convertir a conjunto

            # Obtener parejas de la base de datos
            for persona in trabajadores:
                parejas = GuardshiftDAO().get_duoid(persona)

                # Verificar si se encontraron parejas para la persona
                if parejas:
                    for pareja in parejas:
                        parejasDuo.add(
                            tuple(sorted(pareja)))  # Ordenar la pareja antes de agregarla para evitar duplicados

        except Exception as e:
            print(f"Error al obtener las parejas de trabajadores: {e}")

        lista_aux_iter = iter(list(parejasDuo))
        current_date = begin_date
        insertados = set()  # Inicializado como conjunto
        ultima_insercion = None  # Inicializamos la variable de la última inserción

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person('Trabajador')

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            try:
                                # Intentar obtener el siguiente par de personas de lista_aux
                                persona1, persona2 = next(lista_aux_iter, (None, None))
                                if persona1 is not None and persona2 is not None:
                                    insertados.add(persona1)
                                    insertados.add(persona2)

                                    guardia_dao = GuardshiftDAO()

                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                                    ultima_insercion = current_date  # Actualizamos la variable de la última inserción
                            except Exception as e:
                                print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {'Trabajador'} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {'Trabajador'} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)

        # Después del bucle, ultima_insercion contendrá el día de la última inserción
        if ultima_insercion:
            print("Día de la última inserción:", ultima_insercion)
        else:
            print("No se realizaron inserciones durante el período especificado.")

        current_date = ultima_insercion

        for i in range(0, len(trabajadores), 2):
            persona1 = trabajadores[i][0]
            persona2 = trabajadores[i + 1][0] if i + 1 < len(trabajadores) else None

            # Verificar si hay una pareja y si no está en lista_aux
            if persona2 is not None and ((persona1, persona2) not in parejasporplanificar) and (
                    (persona2, persona1) not in parejasporplanificar):
                parejasporplanificar.add((persona1, persona2))  # Usando add() correctamente

        # Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
        lista_aux_iter2 = iter(list(parejasporplanificar))

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person('Trabajador')

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            persona1, persona2 = next(lista_aux_iter2, (None, None))
                            if persona1 is not None and persona2 is not None:
                                try:
                                    guardia_dao = GuardshiftDAO()

                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                                except Exception as e:
                                    print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {'Trabajador'} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {'Trabajador'} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)

            # Reiniciar el iterador lista_aux_iter2 antes de la próxima iteración si es necesario
            if current_date > end_date:
                lista_aux_iter2 = iter(list(parejasporplanificar))

    def crearTurnoEstudiantesMNoMesPasado(self, begin_date, end_date, rol,sex):

        parejasDuo = set()
        estudiantesM = set()  # Inicializado como conjunto
        parejasporplanificar = set()

        try:
            estudiantesM = GuardshiftDAO().students_without_guard_last_month3('M')  # Convertir a conjunto

            # Obtener parejas de la base de datos
            for persona in estudiantesM:
                parejas = GuardshiftDAO().get_duoid(persona)

                # Verificar si se encontraron parejas para la persona
                if parejas:
                    for pareja in parejas:
                        parejasDuo.add(
                            tuple(sorted(pareja)))  # Ordenar la pareja antes de agregarla para evitar duplicados

        except Exception as e:
            print(f"Error al obtener las parejas de trabajadores: {e}")

        lista_aux_iter = iter(list(parejasDuo))
        current_date = begin_date
        insertados = set()  # Inicializado como conjunto
        ultima_insercion = None  # Inicializamos la variable de la última inserción

        print(parejasDuo)

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person("Estudiante", 'M')

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            try:
                                # Intentar obtener el siguiente par de personas de lista_aux
                                persona1, persona2 = next(lista_aux_iter, (None, None))
                                if persona1 is not None and persona2 is not None:
                                    insertados.add(persona1)
                                    insertados.add(persona2)

                                    guardia_dao = GuardshiftDAO()

                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                                    ultima_insercion = current_date  # Actualizamos la variable de la última inserción
                            except Exception as e:
                                print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {'Trabajador'} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {'Trabajador'} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)

        # Después del bucle, ultima_insercion contendrá el día de la última inserción
        if ultima_insercion:
            print("Día de la última inserción:", ultima_insercion)
        else:
            print("No se realizaron inserciones durante el período especificado.")

        current_date = ultima_insercion

        for i in range(0, len(estudiantesM), 2):
            persona1 = estudiantesM[i][0]
            persona2 = estudiantesM[i + 1][0] if i + 1 < len(estudiantesM) else None

            # Verificar si hay una pareja y si no está en lista_aux
            if persona2 is not None and ((persona1, persona2) not in parejasporplanificar) and (
                    (persona2, persona1) not in parejasporplanificar):
                parejasporplanificar.add((persona1, persona2))  # Usando add() correctamente

        # Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
        lista_aux_iter2 = iter(list(parejasporplanificar))

        print(parejasporplanificar)

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person('Estudiante', 'M')

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            persona1, persona2 = next(lista_aux_iter2, (None, None))
                            if persona1 is not None and persona2 is not None:
                                try:
                                    guardia_dao = GuardshiftDAO()

                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                                except Exception as e:
                                    print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {'Estudiante'} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {'Estudiante'} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)

            # Reiniciar el iterador lista_aux_iter2 antes de la próxima iteración si es necesario
            if current_date > end_date:
                lista_aux_iter2 = iter(list(parejasporplanificar))

    def crearTurnoEstudiantesFNoMesPasado(self, begin_date, end_date, rol,sex):

        parejasDuo = set()
        estudiantesF = set()  # Inicializado como conjunto
        parejasporplanificar = set()

        try:
            estudiantesF = GuardshiftDAO().students_without_guard_last_month3('F')  # Convertir a conjunto

            # Obtener parejas de la base de datos
            for persona in estudiantesF:
                parejas = GuardshiftDAO().get_duoid(persona)

                # Verificar si se encontraron parejas para la persona
                if parejas:
                    for pareja in parejas:
                        parejasDuo.add(
                            tuple(sorted(pareja)))  # Ordenar la pareja antes de agregarla para evitar duplicados

        except Exception as e:
            print(f"Error al obtener las parejas de trabajadores: {e}")

        lista_aux_iter = iter(list(parejasDuo))
        current_date = begin_date
        insertados = set()  # Inicializado como conjunto
        ultima_insercion = None  # Inicializamos la variable de la última inserción

        print(parejasDuo)

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person("Estudiante", 'F')

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            try:
                                # Intentar obtener el siguiente par de personas de lista_aux
                                persona1, persona2 = next(lista_aux_iter, (None, None))
                                if persona1 is not None and persona2 is not None:
                                    insertados.add(persona1)
                                    insertados.add(persona2)

                                    guardia_dao = GuardshiftDAO()

                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                                    ultima_insercion = current_date  # Actualizamos la variable de la última inserción
                            except Exception as e:
                                print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {'Trabajador'} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {'Trabajador'} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)

        # Después del bucle, ultima_insercion contendrá el día de la última inserción
        if ultima_insercion:
            print("Día de la última inserción:", ultima_insercion)
        else:
            print("No se realizaron inserciones durante el período especificado.")

        current_date = ultima_insercion

        for i in range(0, len(estudiantesF), 2):
            persona1 = estudiantesF[i][0]
            persona2 = estudiantesF[i + 1][0] if i + 1 < len(estudiantesF) else None

            # Verificar si hay una pareja y si no está en lista_aux
            if persona2 is not None and ((persona1, persona2) not in parejasporplanificar) and (
                    (persona2, persona1) not in parejasporplanificar):
                parejasporplanificar.add((persona1, persona2))  # Usando add() correctamente

        # Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
        lista_aux_iter2 = iter(list(parejasporplanificar))

        print(parejasporplanificar)

        while current_date <= end_date:
            formatted_date = current_date.strftime("%Y-%m-%d")

            # Verificar si es un día de descanso utilizando el formato
            if not DayOfRestDAO().is_rest_day(formatted_date):
                day_of_week = current_date.strftime("%A")

                schedule_info = ScheduleDAO().get_schedule_for_person('Estudiante', 'F')

                if schedule_info:
                    for day, begin_time, end_time in schedule_info:
                        if day == day_of_week:
                            persona1, persona2 = next(lista_aux_iter2, (None, None))
                            if persona1 is not None and persona2 is not None:
                                try:
                                    guardia_dao = GuardshiftDAO()

                                    guardia_dao.insert_guard_shift(
                                        p_day_month_year=current_date,
                                        p_begin_time=begin_time,
                                        p_end_time=end_time,
                                        p_id_number1=persona1,
                                        p_id_number2=persona2
                                    )

                                    print(
                                        f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                                except Exception as e:
                                    print(f"Error al insertar el turno de guardia: {e}")
                else:
                    print(f"No se encontró un horario para {'Estudiante'} en el día {day_of_week}")
            else:
                print(f"Es día de descanso para {'Estudiante'} el {current_date}")

            # Avanzar al siguiente día
            current_date += timedelta(days=1)

            # Reiniciar el iterador lista_aux_iter2 antes de la próxima iteración si es necesario
            if current_date > end_date:
                lista_aux_iter2 = iter(list(parejasporplanificar))

    def crearTurnoEstudiantesM(self, begin_date, end_date, rol,sex):

        self.crearTurnoEstudiantesMAusentesUltimaGuardia(begin_date,end_date,rol,sex)
        self.crearTurnoEstudiantesMNoMesPasado(begin_date,end_date,rol,sex)


    def crearTurnoEstudiantesF(self, begin_date, end_date, rol, sex):

        self.crearTurnoEstudiantesFAusentesUltimaGuardia(begin_date, end_date, rol, sex)
        self.crearTurnoEstudiantesFNoMesPasado(begin_date, end_date, rol, sex)

    def crearTurnoTrabajadores(self, begin_date, end_date):

        self.crearTurnoEstudiantesMNoMesPasado(begin_date,end_date)
        self.crearTurnoTrabajadoresNoMesPasado((begin_date,end_date))








    
































