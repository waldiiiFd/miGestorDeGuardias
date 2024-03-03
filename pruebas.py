from datetime import datetime, timedelta

from DAO.DayOfRestDAO import DayOfRestDAO
from DAO.GuardshiftDAO import GuardshiftDAO
from DAO.PersonDAO import PersonDAO
from DAO.ScheduleDAO import ScheduleDAO
from DAO.StudentDAO import StudentDAO
from DTO.DayOfRest import DayOfRest
from DTO.Guardshift import GuardShift
from DTO.Person import Person
from DTO.Student import Student

'''
dao2 = StudentDAO()
students = dao2.get_all_students()

if students is not None:
        # Imprimir los estudiantes obtenidos
    for student in students:
        print(student)
else:
    print("Error al obtener todos los estudiantes")




# Crear una instancia de PersonDAO
dao2 = PersonDAO()

# Obtener todos los trabajadores
workers = dao2.get_all_workers()

# Verificar si se obtuvieron los trabajadores correctamente
if workers is not None:
    # Imprimir los trabajadores obtenidos
    for worker in workers:
        print(worker)
else:
    print("Error al obtener todos los trabajadores")




traba = Person("123456", "Juan Perez", "M", "Apto", "Estudiante")
print(traba)

trabadao=PersonDAO()
if trabadao.insert_worker(traba):
    print("insercion exitosa")
else:
    print("Error en la insercion")


traba = Person("123456", "Juan Perez", "M", "Apto", "Trabajador")
print(traba)

trabadao = PersonDAO()

if trabadao.update_person_state(traba.get_id_number(), "No apto"):
    print("Actualizacion exitosa")
else:
    print("Error en la actualizacion")


trabadao = PersonDAO()
person_info = trabadao.get_person_information("123456")  # Cambia "123456" por el número de identificación deseado
if person_info:
    print(person_info)
else:
    print("Error al obtener la información de la persona")

day_of_rest_dao = DayOfRestDAO()

year = 2024
day_of_rest_info = day_of_rest_dao.get_dayofrestinformation_byyear(year)
if day_of_rest_info is not None:
    for day in day_of_rest_info:
        print(day)
else:
    print("No se pudo obtener la información de días no laborables.")


from DAO.DayOfRestDAO import DayOfRestDAO
from DTO.DayOfRest import DayOfRest

start_date = DayOfRest("2024-02-16")
end_date = DayOfRest("2024-03-16")

dayofrest_dao = DayOfRestDAO()
result = dayofrest_dao.insert_daysofrest_in_interval(start_date.get_rest_day_month_year(), end_date.get_rest_day_month_year())

if result:
    print("Días de descanso añadidos exitosamente!")
else:
    print("Error al insertar días de descanso.")


id_number = "830917275"
personDAO = PersonDAO()
result = personDAO.get_person_information(id_number)
if result:
    print(result)
else:
    print("xgustoooooo")

horario =Schedule(id_shedule='123', day_of_week='Monday', begin_time='8:00', end_time='12:00')

print(horario.day_of_week)

estudiante = Student(id_number="123456789", full_name="Jane Doe", sex="Female", current_state="Active", type_person="Student", group="A")

# Imprimir el sexo del estudiante
print(estudiante.get_sex())

estudiante = Student(id_number="02090966545", full_name="Waldo Fernandez Fariñas", sex="M", current_state="Activo", type_person="Estudiante", group="22")

# Crear un objeto StudentDAO
# Crear un objeto StudentDAO
estudianteDao = StudentDAO()

# Llamar al método update_student_group del objeto StudentDAO para actualizar el grupo del estudiante
estudianteDao.update_student_group(estudiante)


dia = DayOfRestDAO()
result=dia.is_rest_day('2024-12-12')
print(result)


# Suponiendo que tengamos una instancia de ScheduleDAO llamada 'schedule_dao'

# Tipo de persona y sexo para los cuales deseamos obtener el horario

shedule = ScheduleDAO()
try:
    # Llamamos a la función para obtener el horario
    schedule_info = shedule.get_schedule_for_person('Estudiante','M')

    if schedule_info:

        print(f"Inicio: {schedule_info[0]}")
        print(f"Fin: {schedule_info[1]}")
    else:
        print("No se encontró un horario para la persona y sexo especificados.")
except Exception as e:
    print(f"Error al obtener el horario: {e}")


guardiasAntiguas = GuardshiftDAO()
personasausentesAsus2UltimasGuardias = guardiasAntiguas.get_missing_shifts()
print(personasausentesAsus2UltimasGuardias)



rol = 'Estudiante'
sex = 'M'
schedule = ScheduleDAO()
schedule_info = schedule.get_schedule_for_person(rol, sex)

print(schedule_info)

for day, begin_time, end_time in schedule_info:
    # day contiene el día de la semana
    print("Día:", day)

    # begin_time contiene la hora de inicio
    print("Hora de inicio:", begin_time)

    # end_time contiene la hora de finalización
    print("Hora de finalización:", end_time)
    
personas_ausentes = GuardshiftDAO().get_missing_shifts()

lista_aux = set()  # Utilizar un conjunto en lugar de una lista

ipersonas_ausentes = GuardshiftDAO().get_missing_shifts()
print(personas_ausentes)

lista_aux = set()  # Utilizar un conjunto en lugar de una lista

# Iterar sobre las personas ausentes para emparejarlas
for i in range(0, len(personas_ausentes), 2):
    # Obtener las dos personas para este par
    persona1 = personas_ausentes[i][0]
    persona2 = personas_ausentes[i + 1][0] if i + 1 < len(personas_ausentes) else None

    # Verificar si ambos están disponibles y no se han emparejado previamente
    if persona2 and ((persona1, persona2) not in lista_aux) and ((persona2, persona1) not in lista_aux):
        lista_aux.add((persona1, persona2))  # Agregar al conjunto
        print(persona1)
        print(persona2)
        print("otro ciclo")

print(lista_aux)    












rol='Estudiante'
sex="M"

start_date = datetime.strptime("2024-03-01", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-08", "%Y-%m-%d").date()

guardia = GuardShift()
result = guardia.crearTurnoGuardiaAutomatico(start_date, end_date, "Estudiante", "M")



from datetime import datetime, timedelta

# Ajustes de los valores de prueba
lista_aux = {('93010700504', '82093006762'), ('83050624520', '86042707727')}
rol = 'Estudiante'
sex = "M"

start_date = datetime.strptime("2024-03-01", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-03", "%Y-%m-%d").date()

current_date = start_date

for persona1, persona2 in lista_aux:
    if current_date <= end_date:
        # Obtener los IDs de las personas
        id1, id2 = persona1, persona2
        print(id1)
        print(id2)
        print(current_date)
        current_date += timedelta(days=1)

    else:
        break  # Salir del bucle si current_date supera end_date



from datetime import datetime, timedelta

# Ajustes de los valores de prueba
lista_aux = [('93010700504', '82093006762'), ('83050624520', '86042707727')]
rol = 'Estudiante'
sex = "M"

start_date = datetime.strptime("2024-03-01", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-03", "%Y-%m-%d").date()

current_date = start_date

# Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
lista_aux_iter = iter(lista_aux)

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

                            print(f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                    except Exception as e:
                        print(f"Error al insertar el turno de guardia: {e}")
        else:
            print(f"No se encontró un horario para {rol} en el día {day_of_week}")
    else:
        print(f"Es día de descanso para {rol} el {current_date}")

    # Avanzar al siguiente día
    current_date += timedelta(days=1)



rol = 'Estudiante'
sex = "M"


start_date = datetime.strptime("2024-03-02", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-03", "%Y-%m-%d").date()

guardia = GuardShift()
result = guardia.crearTurnoEstudiantesMAusentesUltimaGuardia(start_date, end_date, "Estudiante", "M")
result2= guardia.crearTurnoEstudiantesFAusentesUltimaGuardia(start_date, end_date, "Estudiante", "F")
result3= guardia.crearTurnoTrabajadoresAusentesUltimaGuardia(start_date, end_date, "Trabajador")





rol = 'Estudiante'
sex = "F"

horario = ScheduleDAO()

# Almacenar el resultado de get_schedule_for_person en una variable
schedule_result = horario.get_schedule_for_person(rol, sex)

# Imprimir el resultado almacenado en schedule_result
print(schedule_result)



rol = 'Estudiante'
sex = "M"
sex2= "F"


start_date = datetime.strptime("2024-03-02", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-03", "%Y-%m-%d").date()

guardia = GuardShift()
result = guardia.crearTurnoEstudiantesMAusentesUltimaGuardia(start_date, end_date,rol,sex)
result2 = guardia.crearTurnoEstudiantesFAusentesUltimaGuardia(start_date, end_date,rol,sex2)

horario=ScheduleDAO()

mi_horario=horario.get_schedule_for_person(rol,sex2)
print(mi_horario)



from datetime import datetime, timedelta

# Ajustes de los valores de prueba
lista_aux = [('ID_PROFESOR_6', 'ID_PROFESOR_7')]
rol = 'Estudiante'
sex = "F"

start_date = datetime.strptime("2024-03-02", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-03", "%Y-%m-%d").date()

current_date = start_date

# Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
lista_aux_iter = iter(lista_aux)

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

                            print(f"Se insertó un turno de guardia para {persona1} y {persona2} el {formatted_date}")
                    except Exception as e:
                        print(f"Error al insertar el turno de guardia: {e}")
        else:
            print(f"No se encontró un horario para {rol} en el día {day_of_week}")
    else:
        print(f"Es día de descanso para {rol} el {current_date}")

    # Avanzar al siguiente día
    current_date += timedelta(days=1)



rol = 'Estudiante'
rol2='Trabajador'
sex = "M"
sex2= "F"


rol = 'Estudiante'
rol2='Trabajador'
sex = "M"
sex2= "F"

start_date = datetime.strptime("2024-03-02", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-03", "%Y-%m-%d").date()

guardia = GuardShift()

result =  guardia.crearTurnoPersonasAusentesUltimaGuardia(start_date,end_date)



rol = 'Estudiante'
rol2='Trabajador'
sex = "M"
sex2= "F"
start_date = datetime.strptime("2024-03-02", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-05", "%Y-%m-%d").date()

guardia = GuardShift()

result2=guardia.crearTurnoTrabajadoresAusentesUltimaGuardia(start_date,end_date,rol2)








parejas_trabajadores = set()

try:
    # Obtener todas las personas ausentes
    trabajadores = GuardshiftDAO().workers_without_guard_last_month()
    print(trabajadores)
except Exception as e:
    print(f"Error al obtener la: {e}")
    ## get pareja de cada cual
    # ver si la pareja esta en esa lista
    # si esta ver si consider de esa pareja esta en verdadero
    # si esta insertarla
    # si no esta no la insertes

for i in range(0, len(trabajadores), 2):
    persona1 = trabajadores[i][0]
    persona2 = trabajadores[i + 1][0] if i + 1 < len(trabajadores) else None

    # Verificar si hay una pareja y si no está en lista_aux
    if persona2 is not None and ((persona1, persona2) not in parejas_trabajadores) and (
            (persona2, persona1) not in parejas_trabajadores):
        parejas_trabajadores.add((persona1, persona2))  # Usando add() correctamente

# Crear el iterador después de completar el bucle
lista_aux_iter = iter(list(parejas_trabajadores))

print(lista_aux_iter)


rol = 'Estudiante'
rol2 = 'Trabajador'
sex = "M"
sex2 = "F"
start_date = datetime.strptime("2024-03-04", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-10", "%Y-%m-%d").date()
guardia = GuardShift()

result2=guardia.crearTurnoTrabajadoresNoMesPasado(start_date,end_date,rol2)


trabajadores = ['ID_PROFESOR_6', 'ID_PROFESOR_7', 'ID_PROFESOR_35', 'ID_PROFESOR_4']
parejasDuo = set()  # Conjunto para almacenar las parejas de la base de datos
parejas_trabajadores = set()  # Conjunto para almacenar las parejas de trabajadores
personas_emparejadas = set()  # Conjunto para mantener un registro de las personas que ya han sido emparejadas

# Obtener las parejas de la base de datos para cada trabajador
for persona in trabajadores:
    parejas = GuardshiftDAO().get_duoid(persona)  # Recupera las parejas de la base de datos

    # Verificar si se encontraron parejas para la persona
    if parejas:
        for pareja in parejas:
            # Añadir la pareja ordenada al conjunto parejasDuo
            if persona < pareja[0]:
                parejasDuo.add((persona, pareja[0]))
            else:
                parejasDuo.add((pareja[0], persona))

# Crear parejas de trabajadores solo si no están presentes en parejasDuo y no se han agregado previamente
for i in range(len(trabajadores)):
    for j in range(i + 1, len(trabajadores)):
        persona1 = trabajadores[i]
        persona2 = trabajadores[j]

        # Verificar si la pareja de trabajadores no está en parejasDuo, no se ha agregado previamente y
        # las personas no han sido emparejadas antes
        if (persona1, persona2) not in parejasDuo and (persona2, persona1) not in parejasDuo \
                and (persona1, persona2) not in parejas_trabajadores and (persona2, persona1) not in parejas_trabajadores \
                and persona1 not in personas_emparejadas and persona2 not in personas_emparejadas:
            # Verificar si alguna de las personas en la pareja ya está presente en una pareja de parejasDuo
            if any(persona1 in pareja or persona2 in pareja for pareja in parejasDuo):
                continue  # Si ya está presente, continuar con la siguiente iteración
            parejas_trabajadores.add((persona1, persona2))
            # Actualizar el conjunto de personas emparejadas
            personas_emparejadas.update([persona1, persona2])

# Unir las parejas de trabajadores y de la base de datos
parejas_unidas = parejas_trabajadores.union(parejasDuo)



rol = 'Estudiante'
rol2 = 'Trabajador'
sex = "M"
sex2 = "F"
start_date = datetime.strptime("2024-03-04", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-10", "%Y-%m-%d").date()
guardia = GuardShift()

result2=guardia.crearTurnoTrabajadoresNoMesPasado(start_date,end_date,rol2)

'''
parejasDuo = set()  # Conjunto para almacenar las parejas de la base de datos
parejas_trabajadores = set()  # Conjunto para almacenar las parejas de trabajadores
personas_emparejadas = set()  # Conjunto para mantener un registro de las personas que ya han sido emparejadas

try:
    # Obtener todas las personas ausentes
    trabajadores = GuardshiftDAO().workers_without_guard_last_month()
except Exception as e:
    print(f"Error al obtener las personas: {e}")

if trabajadores:
    for persona in trabajadores:
        try:
            # Obtener todas las personas ausentes
            pareja = GuardshiftDAO().get_duoid(persona)
        except Exception as e:
            print(f"Error al obtener las personas ausentes: {e}")

        parejasDuo.add(pareja[0])  # Agregar solo el primer elemento de la pareja a parejasDuo como una cadena de texto




    for i in range(0, len(trabajadores), 2):
        persona1 = trabajadores[i][0]
        persona2 = trabajadores[i + 1][0] if i + 1 < len(trabajadores) else None

        # Verificar si hay una pareja y si no está en lista_aux
        if persona2 is not None and ((persona1, persona2) not in parejas_trabajadores) and (
                (persona2, persona1) not in parejas_trabajadores):
            parejas_trabajadores.add((persona1, persona2))  # Usando add() correctamente

    # Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
lista_aux_iter = iter(list(trabajadores))

for i in range(0, len(estudiantesM_ausentes), 2):
    persona1 = estudiantesM_ausentes[i][0]
    persona2 = estudiantesM_ausentes[i + 1][0] if i + 1 < len(estudiantesM_ausentes) else None

    # Verificar si hay una pareja y si no está en lista_aux
    if persona2 is not None and ((persona1, persona2) not in parejas_estudiantes_ausentes) and (
            (persona2, persona1) not in parejas_estudiantes_ausentes):
        parejas_estudiantes_ausentes.add((persona1, persona2))  # Usando add() correctamente

# Convertir lista_aux a una lista para poder iterar sobre ella de manera secuencial
lista_aux_iter = iter(list(parejas_estudiantes_ausentes))






