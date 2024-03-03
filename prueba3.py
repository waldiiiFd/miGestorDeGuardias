from datetime import datetime
from DTO.Guardshift import GuardShift


rol = 'Estudiante'
rol2 = 'Trabajador'
sex = "M"
sex2 = "F"


start_date = datetime.strptime("2024-03-04", "%Y-%m-%d").date()
end_date = datetime.strptime("2024-03-12", "%Y-%m-%d").date()
guardia = GuardShift()


result1=guardia.crearTurnoTrabajadoresAusentesUltimaGuardia(start_date,end_date)
result2=guardia.crearTurnoTrabajadoresNoMesPasado(start_date,end_date)


result3=guardia.crearTurnoEstudiantesMAusentesUltimaGuardia(start_date,end_date,rol,sex)
result4=guardia.crearTurnoEstudiantesMNoMesPasado(start_date,end_date,rol,sex)


result5=guardia.crearTurnoEstudiantesFNoMesPasado(start_date,end_date,rol,sex2)
resutl6=guardia.crearTurnoEstudiantesFAusentesUltimaGuardia(start_date,end_date,rol,sex2)





