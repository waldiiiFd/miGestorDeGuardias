from datetime import datetime, timedelta
from DAO.DayOfRestDAO import DayOfRestDAO
from DAO.GuardshiftDAO import GuardshiftDAO
from DAO.ScheduleDAO import ScheduleDAO
'''
start_date = datetime.strptime("2024-03-04", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-12", "%Y-%m-%d").date()

parejasDuo = set()
estudiantesF = set()  # Inicializado como conjunto
parejasporplanificar = set()

try:
    estudiantesF = GuardshiftDAO().students_without_guard_last_month('F')  # Convertir a conjunto

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
'''