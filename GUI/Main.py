import traceback

from PyQt6 import uic
from PyQt6.QtCore import QTime
from PyQt6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem

from DAO.DayOfRestDAO import DayOfRestDAO
from DAO.DuoDAO import DuoDAO
from DAO.GuardshiftDAO import GuardshiftDAO
from DAO.PersonDAO import PersonDAO
from DAO.ScheduleDAO import ScheduleDAO
from DAO.StudentDAO import StudentDAO
from DAO.UserDAO import UserDAO
from DTO.DayOfRest import DayOfRest
from DTO.Guardshift import GuardShift
from DTO.Person import Person
from DTO.Schedule import Schedule
from DTO.Student import Student
from DTO.User import User
import re


class Main:
    def __init__(self):
        self.main = uic.loadUi("GUI/Main.ui")
        self.initGUI()
        self.main.showMaximized()

    def initGUI(self):
        self.main.btnCrear_usuario.triggered.connect(self.open_insertUser)
        self.main.btnEliminar_usuario.triggered.connect(self.open_deleteUser)
        self.main.btnActualizar_credenciales.triggered.connect(self.open_updateUser)

        self.main.btnInsertar_dia.triggered.connect(self.open_Insert_DayOfRest)
        self.main.btnInsertar_intervalo.triggered.connect(self.open_Insert_DaysOfRest)
        self.main.btnEliminar_dia.triggered.connect(self.open_Delete_DayOfRest)
        self.main.btnEliminar_intervalo.triggered.connect(self.open_Delete_DaysOfRest)
        self.main.btn_descansoInfo.triggered.connect(self.open_get_DayOfRestInformation)

        self.main.btnInsertarEstudiante.triggered.connect(self.open_InsertarEstudiante)
        self.main.btn_get_infoEstudiantes.triggered.connect(self.open_InfoEstudiantes)
        self.main.btn_get_infoTrabajadores.triggered.connect(self.open_InfoTrabajadores)
        self.main.btnEliminarEstudiante.triggered.connect(self.open_EliminarEstudiante)
        self.main.btnActualizarEstadoEstudiante.triggered.connect(self.open_ActualizarEstadoEstudiante)
        self.main.btnGrupoEstudiante.triggered.connect(self.open_ActualizarGrupoEstudiante)

        self.main.btnInsertarTrabajador.triggered.connect(self.open_InsertarTrabajador)
        self.main.btnEliminarTrabajador.triggered.connect(self.open_EliminarTrabajador)
        self.main.btnActualizarEstadoTrabajador.triggered.connect(self.open_ActualizarEstadoTrabajador)
        self.main.btn_Buscar.triggered.connect(self.open_buscarPersona)

        self.main.actionInsertDuoEstudiante.triggered.connect(self.openInsertarDuoEstudiante)
        self.main.actionInsertDuoTrabajador.triggered.connect(self.openInsertarDuoTrabajador)
        self.main.btnGetInfoPareja.triggered.connect(self.openGetInfoDuo)
        self.main.btnActualizarconsider.triggered.connect(self.openUpdate_Duo_Consider)
        self.main.actionDeletetDuo.triggered.connect(self.openEliminarDuo)

        self.main.btnVerInfoHorarios.triggered.connect(self.openVerInfoGuardia)
        self.main.actionInsertHorario.triggered.connect(self.openInsertarHorario)
        self.main.actionDeleteHorario.triggered.connect(self.openDeleteSchedule)

        self.main.actionManualmente.triggered.connect(self.openInsertGuardM)
        self.main.actionEliminarGuardia.triggered.connect(self.openDeleteGuard)
        self.main.actionProximas_guardias.triggered.connect(self.openGet_upcoming_guardShifts)
        self.main.actionAnteriores_guardias.triggered.connect(self.openGet_previousGuardShift)
        self.main.actionActualizarAsistencia.triggered.connect(self.openUpdate_guard_shift_assistance)
        self.main.actionActualizarParticipantes.triggered.connect(self.openUpdate_guard_shift_changeparticipants)

       # self.main.actionAutomatica_para_estudiante.triggered.connect(self.openGenerate_guard_shift_Student)
    '''
    def openGenerate_guard_shift_Student(self):
        self.AnnadirAutomaticoE = uic.loadUi("GUI/AñadirAutomaticoE.ui")
        self.AnnadirAutomaticoE.lblMensaje2.setText("")
        self.AnnadirAutomaticoE.btnAceptar.clicked.connect(self.insert_data_Generate_guard_shift_Student)
        self.AnnadirAutomaticoE.show()

    def insert_data_Generate_guard_shift_Student(self):
        dia1 = self.AnnadirAutomaticoE.dateEdit.date().toString("yyyy-MM-dd")
        dia2 = self.AnnadirAutomaticoE.dateEdit_3.date().toString("yyyy-MM-dd")
        sexo = self.AnnadirAutomaticoE.comboBox.currentText()
        result = False

        # Verificar el género para elegir el método adecuado para generar los turnos de guardia
        if sexo == "F":
            print(dia1)
            print(dia2)
            print(sexo)
            guardia = GuardShift()
            guardia.crearTurnoEstudiantesF("2024-03-04", "2024-03-12", "Estudiante", 'F')

        else:
            print(dia1)
            print(dia2)
            print(sexo)
            guardia = GuardShift()
            guardia.crearTurnoEstudiantesM(dia1, dia2, "Estudiante", sexo)


        
        if result:
            self.AnnadirAutomaticoE.lblMensaje2.setText("Guardias insertadas exitosamente!")
        else:
            self.AnnadirAutomaticoE.lblMensaje2.setText("Error al insertar las guardias insertadas!")


     '''


    def openUpdate_guard_shift_changeparticipants(self):
        self.update_guard_shift_changeparticipants = uic.loadUi("GUI/Update_guard_shift_changeparticipants.ui")
        self.update_guard_shift_changeparticipants.lblMensaje2.setText("")
        self.update_guard_shift_changeparticipants.btnAceptar.clicked.connect(self.insert_data_Guard_shift_changeparticipants)
        self.update_guard_shift_changeparticipants.show()

        column_widths = [100, 100, 100, 200, 250, 200, 250, 100]
        for col, width in enumerate(column_widths):
            self.update_guard_shift_changeparticipants.tblGuardshift.setColumnWidth(col, width)

        guardShiftDAO = GuardshiftDAO()

        result = guardShiftDAO.get_upcoming_guard_shifts()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.update_guard_shift_changeparticipants.tblGuardshift.setRowCount(num_rows)
            self.update_guard_shift_changeparticipants.tblGuardshift.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.update_guard_shift_changeparticipants.tblGuardshift.setItem(row, col, item)

            self.update_guard_shift_changeparticipants.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.update_guard_shift_changeparticipants.lblMensaje2.setText(
                "No se encontraron guardias futuras")  # Mostrar mensaje de error

    def insert_data_Guard_shift_changeparticipants(self):##############OJO A ESTE METODO ((((( EN POSTGRES FUNCIONA DEBIDAMENTE BIEN))))
            id_number1 = self.update_guard_shift_changeparticipants.txtID.text()
            id_number2 = self.update_guard_shift_changeparticipants.txtID_2.text()

            # Verificar si los números de identificación son válidos
            if (not id_number1.isdigit() or len(id_number1) != 11) or (
                    not id_number2.isdigit() or len(id_number2) != 11):
                self.update_guard_shift_changeparticipants.lblMensaje2.setText("Ingrese un ID válido!")
                self.update_guard_shift_changeparticipants.txtID.setText("")
                self.update_guard_shift_changeparticipants.txtID_2.setText("")
                self.update_guard_shift_changeparticipants.txtID.setFocus()
                return

            # Obtener la fecha, hora de inicio y hora de fin seleccionadas por el usuario
            dia1 = self.update_guard_shift_changeparticipants.dateEdit1.date().toString("yyyy-MM-dd")  # Corregir aquí
            inicio1 = self.update_guard_shift_changeparticipants.timeEdit1.time().toString("hh:mm:ss")
            fin1 = self.update_guard_shift_changeparticipants.timeEdit2.time().toString("hh:mm:ss")

            dia2 = self.update_guard_shift_changeparticipants.dateEdit1_2.date().toString("yyyy-MM-dd")  # Corregir aquí
            inicio2 = self.update_guard_shift_changeparticipants.timeEdit1_2.time().toString("hh:mm:ss")
            fin2 = self.update_guard_shift_changeparticipants.timeEdit2_2.time().toString("hh:mm:ss")

            # Actualizar la asistencia de la guardia en la base de datos
            guardShiftDAO = GuardshiftDAO()

            result = guardShiftDAO.update_guard_shift_changeparticipants(dia1,inicio1,fin1,id_number1,dia2,inicio2,fin2,id_number2)

            if result:
                column_widths = [100, 100, 100, 200, 250, 200, 250, 100]
                for col, width in enumerate(column_widths):
                    self.update_guard_shift_changeparticipants.tblGuardshift.setColumnWidth(col, width)

                    guardShiftDAO = GuardshiftDAO()

                    result = guardShiftDAO.get_previous_guard_shifts()

                    if result:

                        # Configurar el número de filas y columnas en la tabla
                        num_rows = len(result)
                        num_cols = len(result[0]) if num_rows > 0 else 0
                        self.update_guard_shift_changeparticipants.tblGuardshift.setRowCount(num_rows)
                        self.update_guard_shift_changeparticipants.tblGuardshift.setColumnCount(num_cols)

                        # Llenar la tabla con los resultados
                        for row, row_data in enumerate(result):
                            for col, value in enumerate(row_data):
                                # Asegúrate de que los datos se agreguen correctamente a la tabla
                                item = QTableWidgetItem(str(value))
                                self.update_guard_shift_changeparticipants.tblGuardshift.setItem(row, col, item)

                        self.update_guard_shift_changeparticipants.lblMensaje2.setText("")  # Limpiar el mensaje de error
                        self.update_guard_shift_changeparticipants.lblMensaje2.setText("Asistencia actualizada exitosamente")
                        self.update_guard_shift_changeparticipants.txtID.setText("")
                        self.update_guard_shift_changeparticipants.txtID_2.setText("")
                        self.update_guard_shift_changeparticipants.txtID.setFocus()
                    else:

                        self.update_guard_shift_changeparticipants.lblMensaje2.setText(
                            "No se encontraron guardias futuras")  # Mostrar mensaje de error
                else:
                    self.update_guard_shift_changeparticipants.lblMensaje2.setText(
                        "Error al actualizar participantes!")  # Mostrar mensaje de error
                    self.update_guard_shift_changeparticipants.txtID.setText("")
                    self.update_guard_shift_changeparticipants.txtID_2.setText("")
                    self.update_guard_shift_changeparticipants.txtID.setFocus()



    def openUpdate_guard_shift_assistance(self):
        self.update_guard_shift_assistance = uic.loadUi("GUI/Update_guard_shift_assistance.ui")
        self.update_guard_shift_assistance.lblMensaje2.setText("")
        self.update_guard_shift_assistance.btnAceptar.clicked.connect(self.insert_data_Guard_shift_assistance)
        self.update_guard_shift_assistance.show()

        column_widths = [80, 80, 80, 100, 250, 80, 100, 250, 80, 80]
        for col, width in enumerate(column_widths):
            self.update_guard_shift_assistance.tblGuardshift.setColumnWidth(col, width)

        guardShiftDAO = GuardshiftDAO()

        result = guardShiftDAO.get_previous_guard_shifts()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.update_guard_shift_assistance.tblGuardshift.setRowCount(num_rows)
            self.update_guard_shift_assistance.tblGuardshift.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.update_guard_shift_assistance.tblGuardshift.setItem(row, col, item)

            self.update_guard_shift_assistance.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.update_guard_shift_assistance.lblMensaje2.setText(
                "No se encontraron guardias pasadas")  # Mostrar mensaje de error

    def insert_data_Guard_shift_assistance(self):
        # Obtener los números de identificación ingresados por el usuario
        id_number1 = self.update_guard_shift_assistance.txtID.text()
        id_number2 = self.update_guard_shift_assistance.txtID_2.text()

        # Verificar si los números de identificación son válidos
        if (not id_number1.isdigit() or len(id_number1) != 11) or (not id_number2.isdigit() or len(id_number2) != 11):
            self.update_guard_shift_assistance.lblMensaje2.setText("Ingrese un ID válido!")
            self.update_guard_shift_assistance.txtID.setText("")
            self.update_guard_shift_assistance.txtID_2.setText("")
            self.update_guard_shift_assistance.txtID.setFocus()
            return

        else:
            # Obtener el estado de los checkboxes
            check1 = self.update_guard_shift_assistance.checkBox.isChecked()
            check2 = self.update_guard_shift_assistance.checkBox_2.isChecked()

            # Obtener la fecha, hora de inicio y hora de fin seleccionadas por el usuario
            dia = self.update_guard_shift_assistance.dateEdit1.date().toString("yyyy-MM-dd")  # Corregir aquí
            inicio = self.update_guard_shift_assistance.timeEdit1.time().toString("hh:mm:ss")
            fin = self.update_guard_shift_assistance.timeEdit2.time().toString("hh:mm:ss")

            # Actualizar la asistencia de la guardia en la base de datos
            guardShiftDAO = GuardshiftDAO()
            result = guardShiftDAO.update_guard_shift_assistance(dia, inicio, fin, id_number1, id_number2, check1,
                                                                 check2)

            # Manejar el resultado de la operación de actualización
            if result:
                column_widths = [80, 80, 80, 100, 250, 80, 100, 250, 80, 80]
                for col, width in enumerate(column_widths):
                    self.update_guard_shift_assistance.tblGuardshift.setColumnWidth(col, width)

                guardShiftDAO = GuardshiftDAO()

                result = guardShiftDAO.get_previous_guard_shifts()

                if result:
                    # Configurar el número de filas y columnas en la tabla
                    num_rows = len(result)
                    num_cols = len(result[0]) if num_rows > 0 else 0
                    self.update_guard_shift_assistance.tblGuardshift.setRowCount(num_rows)
                    self.update_guard_shift_assistance.tblGuardshift.setColumnCount(num_cols)

                    # Llenar la tabla con los resultados
                    for row, row_data in enumerate(result):
                        for col, value in enumerate(row_data):
                            # Asegúrate de que los datos se agreguen correctamente a la tabla
                            item = QTableWidgetItem(str(value))
                            self.update_guard_shift_assistance.tblGuardshift.setItem(row, col, item)

                    self.update_guard_shift_assistance.lblMensaje2.setText("")  # Limpiar el mensaje de error
                    self.update_guard_shift_assistance.lblMensaje2.setText("Asistencia actualizada exitosamente")
                    self.update_guard_shift_assistance.txtID.setText("")
                    self.update_guard_shift_assistance.txtID_2.setText("")
                    self.update_guard_shift_assistance.txtID.setFocus()


                else:
                    self.update_guard_shift_assistance.lblMensaje2.setText(
                        "No se encontraron guardias futuras")  # Mostrar mensaje de error
                    self.update_guard_shift_assistance.txtID.setText("")
                    self.update_guard_shift_assistance.txtID_2.setText("")
                    self.update_guard_shift_assistance.txtID.setFocus()


            else:
                self.update_guard_shift_assistance.lblMensaje2.setText("Error al actualizar asistencia!")
                self.update_guard_shift_assistance.txtID.setText("")
                self.update_guard_shift_assistance.txtID_2.setText("")
                self.update_guard_shift_assistance.txtID.setFocus()

            self.update_guard_shift_assistance.checkBox.setChecked(False)
            self.update_guard_shift_assistance.checkBox_2.setChecked(False)


    def openGet_previousGuardShift(self):
        self.get_previousGuardShift = uic.loadUi("GUI/Get_previousGuardshift.ui")
        self.get_previousGuardShift.lblMensaje2.setText("")
        self.get_previousGuardShift.show()

        column_widths = [80, 80, 80, 100, 250, 80, 100, 250, 80, 80]
        for col, width in enumerate(column_widths):
            self.get_previousGuardShift.tblGuardshift.setColumnWidth(col, width)

        guardShiftDAO = GuardshiftDAO()

        result = guardShiftDAO.get_previous_guard_shifts()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.get_previousGuardShift.tblGuardshift.setRowCount(num_rows)
            self.get_previousGuardShift.tblGuardshift.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.get_previousGuardShift.tblGuardshift.setItem(row, col, item)

            self.get_previousGuardShift.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.get_previousGuardShift.lblMensaje2.setText(
                "No se encontraron guardias pasadas")  # Mostrar mensaje de error


    def openGet_upcoming_guardShifts(self):
        self.get_upcoming_guard_shifts = uic.loadUi("GUI/Get_upcoming_guardShifts.ui")
        self.get_upcoming_guard_shifts.lblMensaje2.setText("")
        self.get_upcoming_guard_shifts.show()

        column_widths = [100, 100, 100, 200, 250, 200, 250, 100]
        for col, width in enumerate(column_widths):
            self.get_upcoming_guard_shifts.tblGuardshift.setColumnWidth(col, width)

        guardShiftDAO=GuardshiftDAO()

        result = guardShiftDAO.get_upcoming_guard_shifts()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.get_upcoming_guard_shifts.tblGuardshift.setRowCount(num_rows)
            self.get_upcoming_guard_shifts.tblGuardshift.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.get_upcoming_guard_shifts.tblGuardshift.setItem(row, col, item)

            self.get_upcoming_guard_shifts.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.get_upcoming_guard_shifts.lblMensaje2.setText("No se encontraron guardias antiguas")  # Mostrar mensaje de error


    def openDeleteGuard(self):
        self.DeleteGuard = uic.loadUi("GUI/DeleteGuard.ui")
        self.DeleteGuard.lblMensaje2.setText("")
        self.DeleteGuard.btnAceptar.clicked.connect(self.insert_data_DeleteGuard)
        self.DeleteGuard.show()

    def insert_data_DeleteGuard(self):
        date = self.DeleteGuard.dateEdit.text()
        begin = self.DeleteGuard.timeEdit1.time().toString("hh:mm:ss")
        end = self.DeleteGuard.timeEdit2.time().toString("hh:mm:ss")

        guardshiftDAO = GuardshiftDAO()
        result = guardshiftDAO.delete_guard_shift(date,begin,end)

        if result:
            self.DeleteGuard.lblMensaje2.setText("Guardia eliminada exitosamente!")
            self.DeleteGuard.timeEdit1.setTime(QTime(0, 0))  # Reajustar timeEdit1 a las 00:00
            self.DeleteGuard.timeEdit2.setTime(QTime(0, 0))  # Reajustar timeEdit2 a las 00:00

        else:
            self.DeleteGuard.lblMensaje2.setText("Error al eliminada guardia!")
            self.DeleteGuard.timeEdit1.setTime(QTime(0, 0))  # Reajustar timeEdit1 a las 00:00
            self.DeleteGuard.timeEdit2.setTime(QTime(0, 0))  # Reajustar timeEdit2 a las 00:00

    def openInsertGuardM(self):
        self.InsertGuardM = uic.loadUi("GUI/InsertGuardM.ui")
        self.InsertGuardM.lblMensaje2.setText("")
        self.InsertGuardM.btnAceptar.clicked.connect(self.insert_data_InsertGuardM)
        self.InsertGuardM.show()

    def insert_data_InsertGuardM(self):
        id_number1 = self.InsertGuardM.txtID.text()
        id_number2 = self.InsertGuardM.txtID_2.text()

        if (not id_number1.isdigit() or len(id_number1) != 11) or (not id_number2.isdigit() or len(id_number2) != 11):
            self.InsertGuardM.lblMensaje2.setText("Ingrese un ID válido!")
            self.InsertGuardM.txtID.setText("")
            self.InsertGuardM.txtID_2.setText("")
            self.InsertGuardM.txtID.setFocus()
            return
        else:
            date = self.InsertGuardM.dateEdit.text()
            begin = self.InsertGuardM.timeEdit1.time().toString("hh:mm:ss")
            end = self.InsertGuardM.timeEdit2.time().toString("hh:mm:ss")

            guardshiftDAO = GuardshiftDAO()
            result = guardshiftDAO.insert_guard_shift(date,begin,end,id_number1,id_number2)

            if result:
                self.InsertGuardM.lblMensaje2.setText("Guardia añadida exitosamente!")
                self.InsertGuardM.txtID.setText("")
                self.InsertGuardM.txtID_2.setText("")
            else:
                self.InsertGuardM.lblMensaje2.setText("Error al insertar guardia!")
                self.InsertGuardM.txtID.setText("")
                self.InsertGuardM.txtID_2.setText("")
                self.InsertGuardM.txtID.setFocus()





    def openInsertarHorario(self):
        self.InsertSchedule = uic.loadUi("GUI/InsertSchedule.ui")
        self.InsertSchedule.lblMensaje2.setText("")
        self.InsertSchedule.btnAceptar6.clicked.connect(self.insert_data_InsertShedule)
        self.InsertSchedule.show()

        column_widths = [100, 90, 90,100,50]
        for col, width in enumerate(column_widths):
            self.InsertSchedule.tblHorario.setColumnWidth(col, width)

        scheduledao = ScheduleDAO()

        # Obtener los resultados de la consulta
        result = scheduledao.get_all_schedules()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.InsertSchedule.tblHorario.setRowCount(num_rows)
            self.InsertSchedule.tblHorario.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.InsertSchedule.tblHorario.setItem(row, col, item)

            self.InsertSchedule.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.InsertSchedule.lblMensaje2.setText("No se encontraron horarios")  # Mostrar mensaje de error

    def insert_data_InsertShedule(self):
        dia = self.InsertSchedule.comboBox.currentText()
        inicio = self.InsertSchedule.timeEdit1.time().toString("hh:mm:ss")  # Obtener la hora del componente timeEdit1
        fin = self.InsertSchedule.timeEdit2.time().toString("hh:mm:ss")  # Obtener la hora del componente timeEdit2
        rol = self.InsertSchedule.comboBox_2.currentText()
        sexo= self.InsertSchedule.comboBox_3.currentText()

        if sexo == "None":
            sexo = None

        scheduleDAO = ScheduleDAO()
        result = scheduleDAO.insert_schedule(dia, inicio, fin,rol,sexo)

        if result:
            self.InsertSchedule.lblMensaje2.setText("Horario insertado exitosamente!")
            self.InsertSchedule.comboBox.setCurrentIndex(0)  # Reajustar comboBox en Monday
            self.InsertSchedule.timeEdit1.setTime(QTime(0, 0))  # Reajustar timeEdit1 a las 00:00
            self.InsertSchedule.timeEdit2.setTime(QTime(0, 0))  # Reajustar timeEdit2 a las 00:00

            column_widths = [100, 90, 90]
            for col, width in enumerate(column_widths):
                self.InsertSchedule.tblHorario.setColumnWidth(col, width)

            scheduledao = ScheduleDAO()

            # Obtener los resultados de la consulta
            result = scheduledao.get_all_schedules()

            if result:
                # Configurar el número de filas y columnas en la tabla
                num_rows = len(result)
                num_cols = len(result[0]) if num_rows > 0 else 0
                self.InsertSchedule.tblHorario.setRowCount(num_rows)
                self.InsertSchedule.tblHorario.setColumnCount(num_cols)

                # Llenar la tabla con los resultados
                for row, row_data in enumerate(result):
                    for col, value in enumerate(row_data):
                        # Asegúrate de que los datos se agreguen correctamente a la tabla
                        item = QTableWidgetItem(str(value))
                        self.InsertSchedule.tblHorario.setItem(row, col, item)

                # Limpiar mensaje de error
                self.InsertSchedule.lblMensaje2.setText("")
            else:
                self.InsertSchedule.lblMensaje2.setText("No se encontraron horarios")  # Mostrar mensaje de error

        else:
            self.InsertSchedule.lblMensaje2.setText("Error al insertar horario!")  # Mostrar mensaje de error
            self.InsertSchedule.comboBox.setCurrentIndex(0)  # Reajustar comboBox en Monday
            self.InsertSchedule.timeEdit1.setTime(QTime(0, 0))  # Reajustar timeEdit1 a las 00:00
            self.InsertSchedule.timeEdit2.setTime(QTime(0, 0))  # Reajustar timeEdit2 a las 00:00

    def openDeleteSchedule(self):
        self.DeleteSchedule = uic.loadUi("GUI/DeleteSchedule.ui")
        self.DeleteSchedule.lblMensaje2.setText("")
        self.DeleteSchedule.btnAceptar6.clicked.connect(self.insert_data_DeleteShedule)
        self.DeleteSchedule.show()

        column_widths = [100, 90, 90]
        for col, width in enumerate(column_widths):
            self.DeleteSchedule.tblHorario.setColumnWidth(col, width)

        scheduledao = ScheduleDAO()

        # Obtener los resultados de la consulta
        result = scheduledao.get_all_schedules()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.DeleteSchedule.tblHorario.setRowCount(num_rows)
            self.DeleteSchedule.tblHorario.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.DeleteSchedule.tblHorario.setItem(row, col, item)

            self.DeleteSchedule.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.DeleteSchedule.lblMensaje2.setText("No se encontraron horarios")  # Mostrar mensaje de error

    def insert_data_DeleteShedule(self):
        dia = self.DeleteSchedule.comboBox.currentText()
        inicio = self.DeleteSchedule.timeEdit1.time().toString("hh:mm:ss")  # Obtener la hora del componente timeEdit1
        fin = self.DeleteSchedule.timeEdit2.time().toString("hh:mm:ss")  # Obtener la hora del componente timeEdit2

        scheduleDAO = ScheduleDAO()
        result = scheduleDAO.delete_schedule(dia, inicio, fin)

        if result:
            self.DeleteSchedule.lblMensaje2.setText("Horario insertado exitosamente!")
            self.DeleteSchedule.comboBox.setCurrentIndex(0)  # Reajustar comboBox en Monday
            self.DeleteSchedule.timeEdit1.setTime(QTime(0, 0))  # Reajustar timeEdit1 a las 00:00
            self.DeleteSchedule.timeEdit2.setTime(QTime(0, 0))  # Reajustar timeEdit2 a las 00:00

            column_widths = [100, 90, 90]
            for col, width in enumerate(column_widths):
                self.DeleteSchedule.tblHorario.setColumnWidth(col, width)

            scheduledao = ScheduleDAO()

            # Obtener los resultados de la consulta
            result = scheduledao.get_all_schedules()

            if result:
                # Configurar el número de filas y columnas en la tabla
                num_rows = len(result)
                num_cols = len(result[0]) if num_rows > 0 else 0
                self.DeleteSchedule.tblHorario.setRowCount(num_rows)
                self.DeleteSchedule.tblHorario.setColumnCount(num_cols)

                # Llenar la tabla con los resultados
                for row, row_data in enumerate(result):
                    for col, value in enumerate(row_data):
                        # Asegúrate de que los datos se agreguen correctamente a la tabla
                        item = QTableWidgetItem(str(value))
                        self.DeleteSchedule.tblHorario.setItem(row, col, item)

                # Limpiar mensaje de error
                self.DeleteSchedule.lblMensaje2.setText("")
            else:
                self.DeleteSchedule.lblMensaje2.setText("No se encontraron horarios")  # Mostrar mensaje de error

        else:
            self.DeleteSchedule.lblMensaje2.setText("Error al insertar horario!")  # Mostrar mensaje de error
            self.DeleteSchedule.comboBox.setCurrentIndex(0)  # Reajustar comboBox en Monday
            self.DeleteSchedule.timeEdit1.setTime(QTime(0, 0))  # Reajustar timeEdit1 a las 00:00
            self.DeleteSchedule.timeEdit2.setTime(QTime(0, 0))  # Reajustar timeEdit2 a las 00:00

    def openVerInfoGuardia(self):
        self.GetScheduleInfo = uic.loadUi("GUI/GetScheduleInfo.ui")
        self.GetScheduleInfo.lblMensaje2.setText("")
        self.GetScheduleInfo.show()

        column_widths = [100, 90, 90,100,50]
        for col, width in enumerate(column_widths):
            self.GetScheduleInfo.tblHorario.setColumnWidth(col, width)

        scheduledao= ScheduleDAO()

        # Obtener los resultados de la consulta
        result = scheduledao.get_all_schedules()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.GetScheduleInfo.tblHorario.setRowCount(num_rows)
            self.GetScheduleInfo.tblHorario.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.GetScheduleInfo.tblHorario.setItem(row, col, item)

            self.GetScheduleInfo.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.GetScheduleInfo.lblMensaje2.setText("No se encontraron horarios")  # Mostrar mensaje de error


    def openEliminarDuo(self):
        self.DeleteDuo = uic.loadUi("GUI/DeleteDuo.ui")
        self.DeleteDuo.lblMensaje7.setText("")
        self.DeleteDuo.btnAceptar6.clicked.connect(self.insert_data_DeleteDuo)
        self.DeleteDuo.show()

        column_widths = [120, 150, 250, 100, 150, 250, 100, 100]
        for col, width in enumerate(column_widths):
            self.DeleteDuo.tblDuosInfo.setColumnWidth(col, width)

        duoDAO = DuoDAO()

        # Obtener los resultados de la consulta
        result = duoDAO.get_all_duoinformation()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.DeleteDuo.tblDuosInfo.setRowCount(num_rows)
            self.DeleteDuo.tblDuosInfo.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.DeleteDuo.tblDuosInfo.setItem(row, col, item)

            self.DeleteDuo.lblMensaje7.setText("")  # Limpiar el mensaje de error

        else:
            self.DeleteDuo.lblMensaje7.setText("No se encontraron trabajadores")  # Mostrar mensaje de error

    def insert_data_DeleteDuo(self):
        id_number1 = self.DeleteDuo.txtID.text()
        id_number2 = self.DeleteDuo.txtID_2.text()

        duoDAO = DuoDAO()
        result = duoDAO.delete_duo(id_number1,id_number2)

        if result:
            self.DeleteDuo.lblMensaje7.setText("Pareja eliminada exitosamente!")

            column_widths = [120, 150, 250, 100, 150, 250, 100, 100]
            for col, width in enumerate(column_widths):
                self.DeleteDuo.tblDuosInfo.setColumnWidth(col, width)

            duoDAO = DuoDAO()

            # Obtener los resultados de la consulta
            result = duoDAO.get_all_duoinformation()

            if result:
                # Configurar el número de filas y columnas en la tabla
                num_rows = len(result)
                num_cols = len(result[0]) if num_rows > 0 else 0
                self.DeleteDuo.tblDuosInfo.setRowCount(num_rows)
                self.DeleteDuo.tblDuosInfo.setColumnCount(num_cols)

                # Llenar la tabla con los resultados
                for row, row_data in enumerate(result):
                    for col, value in enumerate(row_data):
                        # Asegúrate de que los datos se agreguen correctamente a la tabla
                        item = QTableWidgetItem(str(value))
                        self.DeleteDuo.tblDuosInfo.setItem(row, col, item)
        else:
            self.DeleteDuo.lblMensaje7.setText("Error al eliminar pareja!")

        # Limpiar los campos después de la actualización
        self.DeleteDuo.txtID.setText("")
        self.DeleteDuo.txtID_2.setText("")





    def openUpdate_Duo_Consider(self):
        self.updateDuoConsider = uic.loadUi("GUI/Update_Duo_Consider.ui")
        self.updateDuoConsider.lblMensaje7.setText("")
        self.updateDuoConsider.btnAceptar6.clicked.connect(self.insert_data_Update_Duo_Consider)
        self.updateDuoConsider.show()

        column_widths = [120, 150, 250, 100, 150, 250, 100, 100]
        for col, width in enumerate(column_widths):
            self.updateDuoConsider.tblDuosInfo.setColumnWidth(col, width)

        duoDAO = DuoDAO()

        # Obtener los resultados de la consulta
        result = duoDAO.get_all_duoinformation()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.updateDuoConsider.tblDuosInfo.setRowCount(num_rows)
            self.updateDuoConsider.tblDuosInfo.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.updateDuoConsider.tblDuosInfo.setItem(row, col, item)

            self.updateDuoConsider.lblMensaje7.setText("")  # Limpiar el mensaje de error

        else:
            self.updateDuoConsider.lblMensaje7.setText("No se encontraron trabajadores")  # Mostrar mensaje de error




    def openGetInfoDuo(self):
        self.GetInfoDuos = uic.loadUi("GUI/GetInfoDuos.ui")
        self.GetInfoDuos.lblMensaje2.setText("")
        self.GetInfoDuos.show()

        column_widths = [120, 150, 250, 100, 150, 250, 100, 100]
        for col, width in enumerate(column_widths):
            self.GetInfoDuos.tblDuosInfo.setColumnWidth(col, width)

        duoDAO = DuoDAO()

        # Obtener los resultados de la consulta
        result = duoDAO.get_all_duoinformation()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.GetInfoDuos.tblDuosInfo.setRowCount(num_rows)
            self.GetInfoDuos.tblDuosInfo.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    # Asegúrate de que los datos se agreguen correctamente a la tabla
                    item = QTableWidgetItem(str(value))
                    self.GetInfoDuos.tblDuosInfo.setItem(row, col, item)

            self.GetInfoDuos.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.GetInfoDuos.lblMensaje2.setText("No se encontraron trabajadores")  # Mostrar mensaje de error




    def openInsertarDuoEstudiante(self):
        self.InsertParejaStudent= uic.loadUi("GUI/InsertDuoStudent.ui")
        self.InsertParejaStudent.btnAceptar6.clicked.connect(self.insert_data_InsertParejaStudent)
        self.InsertParejaStudent.lblMensaje7.setText("")
        self.InsertParejaStudent.show()

        column_widths = [200, 300, 50, 100, 100]
        for col, width in enumerate(column_widths):
            self.InsertParejaStudent.tblStudent.setColumnWidth(col, width)

        studentDAO = StudentDAO()

        # Obtener los resultados de la consulta
        result = studentDAO.get_all_students()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.InsertParejaStudent.tblStudent.setRowCount(num_rows)
            self.InsertParejaStudent.tblStudent.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.InsertParejaStudent.tblStudent.setItem(row, col, item)

            self.InsertParejaStudent.lblMensaje7.setText("")  # Limpiar el mensaje de error

        else:
            self.Get_InfoStudent.lblMensaje7.setText("No se encontraron estudiantes")  # Mostrar mensaje de error

    def openInsertarDuoTrabajador(self):
        self.InsertParejaWorker = uic.loadUi("GUI/InsertDuoWorker.ui")
        self.InsertParejaWorker.btnAceptar6.clicked.connect(self.insert_data_InsertParejaWorker)
        self.InsertParejaWorker.lblMensaje7.setText("")
        self.InsertParejaWorker.show()

        # Configurar el ancho de las columnas
        column_widths = [200, 300, 50, 100, 100]
        for col, width in enumerate(column_widths):
            self.InsertParejaWorker.tblWorker.setColumnWidth(col, width)

        workerDAO = PersonDAO()

        # Obtener los resultados de la consulta
        result = workerDAO.get_all_workers()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.InsertParejaWorker.tblWorker.setRowCount(num_rows)
            self.InsertParejaWorker.tblWorker.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.InsertParejaWorker.tblWorker.setItem(row, col, item)

            self.InsertParejaWorker.lblMensaje7.setText("")  # Limpiar el mensaje de error

        else:
            self.InsertParejaWorker.lblMensaje7.setText("No se encontraron trabajadores")  # Mostrar mensaje de error

    def open_buscarPersona(self):
        self.get_Person = uic.loadUi("GUI/Get_Person.ui")
        self.get_Person.btnB.clicked.connect(self.insert_data_buscarPersona)
        self.get_Person.lblMensaje2.setText("")
        self.get_Person.show()

        self.get_Person.tblPersona.setColumnWidth(0, 200)
        self.get_Person.tblPersona.setColumnWidth(1, 300)
        self.get_Person.tblPersona.setColumnWidth(2, 50)
        self.get_Person.tblPersona.setColumnWidth(3, 100)
        self.get_Person.tblPersona.setColumnWidth(4, 100)
        self.get_Person.tblPersona.setColumnWidth(5, 100)
        self.get_Person.tblPersona.setColumnWidth(6, 120)

    def open_insertUser(self):
        self.insert_userW = uic.loadUi("GUI/Insert_User.ui")
        self.insert_userW.btnAceptar.clicked.connect(self.insert_data_insertUser)
        self.insert_userW.lblMensaje2.setText("")
        self.insert_userW.show()

    def open_deleteUser(self):
        self.delete_userW = uic.loadUi("GUI/Delete_User.ui")
        self.delete_userW.btnAceptar2.clicked.connect(self.insert_data_deleteUser)
        self.delete_userW.lblMensaje3.setText("")
        self.delete_userW.show()

    def open_updateUser(self):
        self.update_userW = uic.loadUi("GUI/Update_User.ui")
        self.update_userW.btnAceptar3.clicked.connect(self.insert_data_updateUser)
        self.update_userW.lblMensaje4.setText("")
        self.update_userW.show()

    def open_get_DayOfRestInformation(self):
        self.get_DayOfRestInformation = uic.loadUi("GUI/Get_DayOfRestInformation.ui")
        self.get_DayOfRestInformation.lblMensaje2.setText("")
        self.get_DayOfRestInformation.btnB.clicked.connect(self.insert_data_dayOfRestInformation)
        self.get_DayOfRestInformation.show()
        self.get_DayOfRestInformation.tblDescanso.setColumnWidth(2, 90)

    def insert_data_InsertParejaStudent(self):
        id_number1 = self.InsertParejaStudent.txtID.text()
        id_number2= self.InsertParejaStudent.txtID_2.text()

        duoDAO = DuoDAO()
        result = duoDAO.insert_duo(id_number1,id_number2)

        if result:
            self.InsertParejaStudent.lblMensaje7.setText("Pareja añadida exitosamente!")
            self.InsertParejaStudent.txtID.setText("")
            self.InsertParejaStudent.txtID_2.setText("")
        else:
            self.InsertParejaStudent.lblMensaje7.setText("Error al insertar pareja!")
            self.InsertParejaStudent.txtID.setText("")
            self.InsertParejaStudent.txtID_2.setText("")

    def insert_data_Update_Duo_Consider(self):

        id_number1 = self.updateDuoConsider.txtID.text()
        id_number2 = self.updateDuoConsider.txtID_2.text()
        consider = self.updateDuoConsider.checkBox.isChecked()  # Obtener el estado del checkbox

        duoDAO = DuoDAO()
        result = duoDAO.update_duo_consider_by_id(id_number1, id_number2, consider)

        if result:
            self.updateDuoConsider.lblMensaje7.setText("Pareja actualizada exitosamente!")

            column_widths = [120, 150, 250, 100, 150, 250, 100, 100]
            for col, width in enumerate(column_widths):
                self.updateDuoConsider.tblDuosInfo.setColumnWidth(col, width)

            duoDAO = DuoDAO()

            # Obtener los resultados de la consulta
            result = duoDAO.get_all_duoinformation()

            if result:
                # Configurar el número de filas y columnas en la tabla
                num_rows = len(result)
                num_cols = len(result[0]) if num_rows > 0 else 0
                self.updateDuoConsider.tblDuosInfo.setRowCount(num_rows)
                self.updateDuoConsider.tblDuosInfo.setColumnCount(num_cols)

                # Llenar la tabla con los resultados
                for row, row_data in enumerate(result):
                    for col, value in enumerate(row_data):
                        # Asegúrate de que los datos se agreguen correctamente a la tabla
                        item = QTableWidgetItem(str(value))
                        self.updateDuoConsider.tblDuosInfo.setItem(row, col, item)
        else:
            self.updateDuoConsider.lblMensaje7.setText("Error al actualizar pareja!")

        # Limpiar los campos después de la actualización
        self.updateDuoConsider.txtID.setText("")
        self.updateDuoConsider.txtID_2.setText("")
        self.updateDuoConsider.checkBox.setChecked(False)


    def insert_data_InsertParejaWorker(self):
        id_number1 = self.InsertParejaWorker.txtID.text()
        id_number2 = self.InsertParejaWorker.txtID_2.text()

        duoDAO = DuoDAO()
        result = duoDAO.insert_duo(id_number1, id_number2)

        if result:
            self.InsertParejaWorker.lblMensaje7.setText("Pareja añadida exitosamente!")
            self.InsertParejaWorker.txtID.setText("")
            self.InsertParejaWorker.txtID_2.setText("")
        else:
            self.InsertParejaWorker.lblMensaje7.setText("Error al insertar pareja!")
            self.InsertParejaWorker.txtID.setText("")
            self.InsertParejaWorker.txtID_2.setText("")

    def insert_data_dayOfRestInformation(self):
        year = self.get_DayOfRestInformation.txt_anno.text()

        if not year.isdigit() or len(year) != 4:
            self.get_DayOfRestInformation.lblMensaje2.setText("Ingrese un año válido!")
            self.get_DayOfRestInformation.txt_anno.setText("")
            self.get_DayOfRestInformation.txt_anno.setFocus()
            return

        else:
            dateDAO = DayOfRestDAO()
            result = dateDAO.get_dayofrestinformation_byyear(year)

            if result:
                # Limpiamos la tabla y configuramos el resultado en las filas correspondientes
                self.get_DayOfRestInformation.tblDescanso.clearContents()
                self.get_DayOfRestInformation.tblDescanso.setRowCount(len(result))
                for row, row_data in enumerate(result):
                    date_obj = row_data[0]  # Extraemos el objeto datetime.date de la tupla
                    day = date_obj.day
                    month = date_obj.month
                    year = date_obj.year
                    self.get_DayOfRestInformation.tblDescanso.setItem(row, 0,
                                                                      QTableWidgetItem(str(day)))  # Columna del día
                    self.get_DayOfRestInformation.tblDescanso.setItem(row, 1,
                                                                      QTableWidgetItem(str(month)))  # Columna del mes
                    self.get_DayOfRestInformation.tblDescanso.setItem(row, 2,
                                                                      QTableWidgetItem(str(year)))  # Columna del año
                self.get_DayOfRestInformation.lblMensaje2.setText("")  # Limpiamos el mensaje de error
            else:
                self.get_DayOfRestInformation.lblMensaje2.setText("No hay información!")
                self.get_DayOfRestInformation.tblDescanso.clearContents()
                self.get_DayOfRestInformation.txt_anno.setText("")
                self.get_DayOfRestInformation.txt_anno.setFocus()

    def open_Insert_DayOfRest(self):
        self.insert_dayOfRestW = uic.loadUi("GUI/Insert_DayOfRest.ui")
        self.insert_dayOfRestW.btnAceptar4.clicked.connect(self.insert_data_insertDayOfRest)
        self.insert_dayOfRestW.lblMensaje5.setText("")
        self.insert_dayOfRestW.show()

    def open_Insert_DaysOfRest(self):
        self.insert_daysOfRestW = uic.loadUi("GUI/Insert_DaysOfRest.ui")
        self.insert_daysOfRestW.btnAceptar6.clicked.connect(self.insert_data_insertDaysOfRest)
        self.insert_daysOfRestW.lblMensaje7.setText("")
        self.insert_daysOfRestW.show()

    def open_Delete_DayOfRest(self):
        self.delete_dayOfRestW = uic.loadUi("GUI/Delete_DayOfRest.ui")
        self.delete_dayOfRestW.btnAceptar5.clicked.connect(self.insert_data_deleteDayOfRest)
        self.delete_dayOfRestW.lblMensaje6.setText("")
        self.delete_dayOfRestW.show()

    def open_Delete_DaysOfRest(self):
        self.delete_daysOfRestW = uic.loadUi("GUI/Delete_DaysOfRest.ui")
        self.delete_daysOfRestW.btnAceptar7.clicked.connect(self.insert_data_deleteDaysOfRest)
        self.delete_daysOfRestW.lblMensaje8.setText("")
        self.delete_daysOfRestW.show()

    def open_InfoTrabajadores(self):
        self.Get_InfoWorkers = uic.loadUi("GUI/Get_InfoWorkers.ui")
        self.Get_InfoWorkers.show()

        # Configurar el ancho de las columnas
        column_widths = [200, 300, 50, 100, 100]
        for col, width in enumerate(column_widths):
            self.Get_InfoWorkers.tblWorkers.setColumnWidth(col, width)

        workerDAO = PersonDAO()

        # Obtener los resultados de la consulta
        result = workerDAO.get_all_workers()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.Get_InfoWorkers.tblWorkers.setRowCount(num_rows)
            self.Get_InfoWorkers.tblWorkers.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.Get_InfoWorkers.tblWorkers.setItem(row, col, item)

            self.Get_InfoWorkers.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.Get_InfoWorkers.lblMensaje2.setText("No se encontraron trabajadores")  # Mostrar mensaje de error

    def open_InfoEstudiantes(self):
        self.Get_InfoStudent = uic.loadUi("GUI/Get_InfoStudent.ui")
        self.Get_InfoStudent.show()

        # Configurar el ancho de las columnas
        column_widths = [200, 300, 50, 100, 100]
        for col, width in enumerate(column_widths):
            self.Get_InfoStudent.tblStudent.setColumnWidth(col, width)

        studentDAO = StudentDAO()

        # Obtener los resultados de la consulta
        result = studentDAO.get_all_students()

        if result:
            # Configurar el número de filas y columnas en la tabla
            num_rows = len(result)
            num_cols = len(result[0]) if num_rows > 0 else 0
            self.Get_InfoStudent.tblStudent.setRowCount(num_rows)
            self.Get_InfoStudent.tblStudent.setColumnCount(num_cols)

            # Llenar la tabla con los resultados
            for row, row_data in enumerate(result):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.Get_InfoStudent.tblStudent.setItem(row, col, item)

            self.Get_InfoStudent.lblMensaje2.setText("")  # Limpiar el mensaje de error

        else:
            self.Get_InfoStudent.lblMensaje2.setText("No se encontraron estudiantes")  # Mostrar mensaje de error

    def open_InsertarEstudiante(self):
        self.insert_studentW = uic.loadUi("GUI/Insert_Student.ui")
        self.insert_studentW.btnAceptar.clicked.connect(self.insert_data_insertStudent)
        self.insert_studentW.lblMensaje2.setText("")
        self.insert_studentW.show()

    def open_ActualizarGrupoEstudiante(self):
        self.UpdateGroup = uic.loadUi("GUI/UpdateGroup.ui")
        self.UpdateGroup.btnAceptar.clicked.connect(self.insert_data_UpdateGroupStudent)
        self.UpdateGroup.lblMensaje2.setText("")
        self.UpdateGroup.show()

    def open_EliminarEstudiante(self):
        self.delete_PersonW = uic.loadUi("GUI/Delete_Person.ui")
        self.delete_PersonW.btnAceptar.clicked.connect(self.insert_data_DeleteStudent)
        self.delete_PersonW.lblMensaje6.setText("")
        self.delete_PersonW.show()

    def open_ActualizarEstadoEstudiante(self):
        self.update_State = uic.loadUi("GUI/Update_State.ui")
        self.update_State.btnAceptar.clicked.connect(self.insert_data_UpdateStudent)
        self.update_State.lblMensaje2.setText("")
        self.update_State.show()

    def open_ActualizarEstadoTrabajador(self):
        self.update_State = uic.loadUi("GUI/Update_State.ui")
        self.update_State.btnAceptar.clicked.connect(self.insert_data_UpdateWorker)
        self.update_State.lblMensaje2.setText("")
        self.update_State.show()

    def open_InsertarTrabajador(self):
        self.insert_workerW = uic.loadUi("GUI/Insert_Worker.ui")
        self.insert_workerW.btnAceptar.clicked.connect(self.insert_data_insertWorker)
        self.insert_workerW.lblMensaje2.setText("")
        self.insert_workerW.show()

    def insert_data_buscarPersona(self):
        id_number = self.get_Person.txt_ID.text()
        personDAO = PersonDAO()

        result = personDAO.get_person_information(id_number)

        if result:
            # Limpiamos la tabla y configuramos el resultado en la primera fila
            self.get_Person.tblPersona.clearContents()
            self.get_Person.tblPersona.setRowCount(1)
            for col, value in enumerate(result):
                self.get_Person.tblPersona.setItem(0, col, QTableWidgetItem(str(value)))
            self.get_Person.lblMensaje2.setText("")  # Limpiamos el mensaje de error
            self.get_Person.txt_ID.setText("")
        else:
            self.get_Person.tblPersona.clearContents()  # Limpiamos la tabla si no hay resultados
            self.get_Person.lblMensaje2.setText("Persona no encontrada!")  # Mostramos mensaje de error
            self.get_Person.txt_ID.setText("")

    def insert_data_insertWorker(self):
        id_number = self.insert_workerW.txtID.text()
        full_name = self.insert_workerW.txtname.text()

        if not id_number.isdigit() or len(id_number) != 11:
            self.insert_workerW.lblMensaje2.setText("Ingrese un ID válido!")
            self.clear_insert_worker_fields()
            self.insert_workerW.txtID.setFocus()
            return

        if not re.match(r'^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$', full_name):
            self.insert_workerW.lblMensaje2.setText("Ingrese un nombre válido!")
            self.clear_insert_worker_fields()
            self.insert_workerW.txtname.setFocus()
            return

        self.insert_workerW.lblMensaje2.setText("")

        sex = self.insert_workerW.comboBox.currentText()
        current_state = self.insert_workerW.comboBox_2.currentText()

        worker = Person(id_number=id_number, full_name=full_name, current_state=current_state, sex=sex,
                        type_person=None)

        student_dao = PersonDAO()
        result = student_dao.insert_worker(worker)

        if result:
            self.insert_workerW.lblMensaje2.setText("Trabajador añadido exitosamente!")
            self.clear_insert_worker_fields()
        else:
            self.insert_workerW.lblMensaje2.setText("Error al insertar trabajador!")

    def open_EliminarTrabajador(self):
        self.delete_PersonW = uic.loadUi("GUI/Delete_Person.ui")
        self.delete_PersonW.btnAceptar.clicked.connect(self.insert_data_DeleteWorker)
        self.delete_PersonW.lblMensaje6.setText("")
        self.delete_PersonW.show()

    def insert_data_deleteDaysOfRest(self):
        self.delete_daysOfRestW.lblMensaje8.setText("")

        start_date = self.delete_daysOfRestW.dateEdit1.text()
        end_date = self.delete_daysOfRestW.dateEdit_2.text()

        dayofrest_dao = DayOfRestDAO()
        result = dayofrest_dao.delete_daysofrest_in_interval(start_date, end_date)

        if result:
            self.delete_daysOfRestW.lblMensaje8.setText("Días de descanso eliminados exitosamente!")
        else:
            self.delete_daysOfRestW.lblMensaje8.setText("Error al eliminar días de descanso.")

    def insert_data_insertDaysOfRest(self):

        self.insert_daysOfRestW.lblMensaje7.setText("")

        start_date = self.insert_daysOfRestW.dateEdit1.text()
        end_date = self.insert_daysOfRestW.dateEdit_2.text()

        dayofrest_dao = DayOfRestDAO()
        result = dayofrest_dao.insert_daysofrest_in_interval(start_date, end_date)

        if result:
            self.insert_daysOfRestW.lblMensaje7.setText("Días de descanso añadidos exitosamente!")
        else:
            self.insert_daysOfRestW.lblMensaje7.setText("Error al insertar días de descanso.")

    def insert_data_deleteDayOfRest(self):
        self.delete_dayOfRestW.lblMensaje6.setText("")
        dayofrest = DayOfRest(rest_day_month_year=self.delete_dayOfRestW.dateEdit.text())
        dayofrest_dao = DayOfRestDAO()
        result = dayofrest_dao.delete_dayofrest(dayofrest)
        if result:
            self.delete_dayOfRestW.lblMensaje6.setText("Día de descanso eliminado exitosamente!")

        else:
            self.delete_dayOfRestW.lblMensaje6.setText("Error de eliminación!")

    def insert_data_insertDayOfRest(self):
        self.insert_dayOfRestW.lblMensaje5.setText("")
        dayofrest = DayOfRest(rest_day_month_year=self.insert_dayOfRestW.dateEdit.text())
        dayofrest_dao = DayOfRestDAO()
        result = dayofrest_dao.insert_dayofrest(dayofrest)
        if result:
            self.insert_dayOfRestW.lblMensaje5.setText("Día de descanso añadido exitosamente!")

        else:
            self.insert_dayOfRestW.lblMensaje5.setText("Error de inserción!")

    def insert_data_insertUser(self):
        if len(self.insert_userW.txtUsuario2.text()) < 2:
            self.insert_userW.lblMensaje2.setText("Ingrese un usuario válido!")
            self.clear_insert_user_fields()
            self.insert_userW.txtUsuario2.setFocus()
        elif len(self.insert_userW.txtClave2.text()) < 2:
            self.insert_userW.lblMensaje2.setText("Ingrese una contraseña válida!")
            self.clear_insert_user_fields()
            self.insert_userW.txtClave2.setFocus()
        elif self.insert_userW.txtClave2.text() != self.insert_userW.txtClave3.text():
            self.insert_userW.lblMensaje2.setText("Las contraseñas no coinciden!")
            self.clear_insert_user_fields()
            self.insert_userW.txtClave2.setFocus()
        else:
            self.insert_userW.lblMensaje2.setText("")
            user = User(username=self.insert_userW.txtUsuario2.text(), password=self.insert_userW.txtClave2.text())
            user_dao = UserDAO()
            result = user_dao.insert_user(user)
            if result:
                self.insert_userW.lblMensaje2.setText("Usuario añadido exitosamente!")
                self.clear_insert_user_fields()
            else:
                self.insert_userW.lblMensaje2.setText("Error de inserción!")
                self.clear_insert_user_fields()

    def insert_data_updateUser(self):
        if len(self.update_userW.txtUsuario5.text()) < 2:
            self.update_userW.lblMensaje2.setText("Ingrese un usuario válido!")
            self.clear_update_user_fields()
            self.update_userW.txtUsuario4.setFocus()

        elif len(self.update_userW.txtClave6.text()) < 2:
            self.update_userW.lblMensaje2.setText("Ingrese una contraseña válida!")
            self.clear_update_user_fields()
            self.update_userW.txtClave6.setFocus()

        elif self.update_userW.txtClave6.text() != self.update_userW.txtClave7.text():
            self.update_userW.lblMensaje2.setText("Las contraseñas no coinciden!")
            self.clear_update_user_fields()
            self.update_userW.txtClave6.setFocus()

        else:
            username = self.update_userW.txtUsuario4.text()
            password = self.update_userW.txtClave5.text()

            new_username = self.update_userW.txtUsuario5.text()
            new_password = self.update_userW.txtClave6.text()

            userDAO = UserDAO()
            result = userDAO.update_user_credentials(username, password, new_username, new_password)

            if result:
                self.update_userW.lblMensaje4.setText("Usuario actualizado exitosamente!")
                self.clear_update_user_fields()
            else:
                self.update_userW.lblMensaje4.setText("Error al actualizar el usuario!")
                self.clear_update_user_fields()
                self.update_userW.txtClave5.setFocus()

    def insert_data_deleteUser(self):
        if len(self.delete_userW.txtUsuario3.text()) < 2:
            self.delete_userW.lblMensaje3.setText("Ingrese un usuario válido!")
            self.clear_delete_user_fields()
            self.delete_userW.txtUsuario3.setFocus()

        elif len(self.delete_userW.txtClave4.text()) < 2:
            self.delete_userW.lblMensaje3.setText("Ingrese una contraseña válida!")
            self.clear_delete_user_fields()
            self.delete_userW.txtClave4.setFocus()

        else:
            self.delete_userW.lblMensaje3.setText("")
            username = self.delete_userW.txtUsuario3.text()
            password = self.delete_userW.txtClave4.text()
            user_dao = UserDAO()
            result = user_dao.delete_user(username, password)

            if result:
                self.delete_userW.lblMensaje3.setText("Usuario eliminado exitosamente!")
                self.clear_delete_user_fields()
            else:
                self.delete_userW.lblMensaje3.setText("Error de eliminación!")
                self.clear_delete_user_fields()
                self.delete_userW.txtUsuario3.setFocus()

    def insert_data_insertStudent(self):
        id_number = self.insert_studentW.txtID.text()
        full_name = self.insert_studentW.txtname.text()
        group = self.insert_studentW.txtGrupo.text()

        if not id_number.isdigit() or len(id_number) != 11:
            self.insert_studentW.lblMensaje2.setText("Ingrese un ID válido!")
            self.clear_insert_student_fields()
            self.insert_studentW.txtID.setFocus()
            return

        if not re.match(r'^[a-zA-ZÁÉÍÓÚáéíóúÑñ\s]+$', full_name):
            self.insert_studentW.lblMensaje2.setText("Ingrese un nombre válido!")
            self.clear_insert_student_fields()
            self.insert_studentW.txtname.setFocus()
            return

        if not group.isdigit() or len(group) != 2:
            self.insert_studentW.lblMensaje2.setText("Ingrese un grupo válido!")
            self.clear_insert_student_fields()
            self.insert_studentW.txtGrupo.setFocus()
            return

        self.insert_studentW.lblMensaje2.setText("")

        sex = self.insert_studentW.comboBox.currentText()
        current_state = self.insert_studentW.comboBox_2.currentText()

        student = Student(id_number=id_number, full_name=full_name, sex=sex, current_state=current_state, group=group,
                          type_person=None)

        student_dao = StudentDAO()
        result = student_dao.insert_student(student)

        if result:
            self.insert_studentW.lblMensaje2.setText("Estudiante añadido exitosamente!")
            self.clear_insert_student_fields()
        else:
            self.insert_studentW.lblMensaje2.setText("Error al insertar estudiante!")
            self.clear_insert_student_fields()
            self.insert_studentW.txtname.setFocus()

    def insert_data_UpdateGroupStudent(self):
        id_number = self.UpdateGroup.txtID.text()
        group = self.UpdateGroup.txtgroup.text()

        student = Student(id_number=id_number, group=group, full_name=None, sex=None, current_state=None,
                          type_person=None)

        student_dao = StudentDAO()
        result = student_dao.update_student_group(student)

        if result:
            self.UpdateGroup.lblMensaje2.setText("Grupo actualizado exitosamente!")
            self.UpdateGroup.txtID.setText("")
            self.UpdateGroup.txtgroup.setText("")
        else:
            self.UpdateGroup.lblMensaje2.setText("Error al actualizar el grupo!")
            self.UpdateGroup.txtID.setText("")
            self.UpdateGroup.txtgroup.setText("")

    def insert_data_DeleteStudent(self):
        id_number = self.delete_PersonW.txtID.text()

        student_dao = PersonDAO()

        result = student_dao.delete_person(id_number)

        if result:
            self.delete_PersonW.lblMensaje6.setText("Eliminado exitosamente!")
            self.delete_PersonW.txtID.setText("")
        else:
            self.delete_PersonW.lblMensaje6.setText("Error al eliminar!")
            self.delete_PersonW.txtID.setText("")

    def insert_data_DeleteWorker(self):
        id_number = self.delete_PersonW.txtID.text()

        worker_dao = PersonDAO()

        result = worker_dao.delete_person(id_number)

        if result:
            self.delete_PersonW.lblMensaje6.setText("Eliminado exitosamente!")
            self.delete_PersonW.txtID.setText("")
        else:
            self.delete_PersonW.lblMensaje6.setText("Error al eliminar!")
            self.delete_PersonW.txtID.setText("")

    def insert_data_UpdateStudent(self):
        id_number = self.update_State.txtID.text()
        state = self.update_State.comboBox_2.currentText()

        student_dao = PersonDAO()
        result = student_dao.update_person_state(id_number, state)

        if result:
            self.update_State.lblMensaje2.setText("Estado actualizado exitosamente!")
            self.update_State.txtID.setText("")
        else:
            self.update_State.lblMensaje2.setText("Error al actualizar el estado!")
            self.update_State.txtID.setText("")

    def insert_data_UpdateWorker(self):
        id_number = self.update_State.txtID.text()
        state = self.update_State.comboBox_2.currentText()

        student_dao = PersonDAO()
        result = student_dao.update_person_state(id_number, state)

        if result:
            self.update_State.lblMensaje2.setText("Estado actualizado exitosamente!")
            self.update_State.txtID.setText("")
        else:
            self.update_State.lblMensaje2.setText("Error al actualizar el estado!")
            self.update_State.txtID.setText("")

    def clear_delete_user_fields(self):
        self.delete_userW.txtUsuario3.setText("")
        self.delete_userW.txtClave4.setText("")

    def clear_insert_user_fields(self):
        self.insert_userW.txtUsuario2.setText("")
        self.insert_userW.txtClave2.setText("")
        self.insert_userW.txtClave3.setText("")

    def clear_update_user_fields(self):
        self.update_userW.txtUsuario4.setText("")
        self.update_userW.txtUsuario5.setText("")
        self.update_userW.txtClave5.setText("")
        self.update_userW.txtClave6.setText("")
        self.update_userW.txtClave7.setText("")

    def clear_insert_student_fields(self):
        self.insert_studentW.txtID.setText("")
        self.insert_studentW.txtname.setText("")
        self.insert_studentW.txtGrupo.setText("")

    def clear_insert_worker_fields(self):
        self.insert_workerW.txtID.setText("")
        self.insert_workerW.txtname.setText("")







