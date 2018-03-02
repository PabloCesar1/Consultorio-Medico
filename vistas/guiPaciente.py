from PyQt5 import uic, QtWidgets, QtGui, QtCore #importamos uic y QtWidgets desde el modulo PyQt5
import sys
import psycopg2
import datetime
import time
sys.path.append('Datos') 
from Paciente import *

qtPaciente = 'diseno/paciente.ui'
Ui_Paciente, QtBaseClass4 = uic.loadUiType(qtPaciente)
class viewPaciente(QtWidgets.QMainWindow, Ui_Paciente):
    def __init__(self,interfaz):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Paciente.__init__(self) 
        self.setupUi(self)
        self.Paciente = Paciente()
        self.RellenarTabla()
        self.listaEmpleados.setSelectionBehavior(QtWidgets.QTableWidget.SelectRows) # seleccionar solo filas
        self.listaEmpleados.setSelectionMode(QtWidgets.QTableWidget.SingleSelection)
        self.interfaz = interfaz
        self.listaEmpleados.itemDoubleClicked.connect(self.EditPaciente)
        self.btnEliminar.clicked.connect(self.dropPaciente)
        self.btnBuscar.clicked.connect(self.Filtrar)


    def RellenarTabla(self):
        self.listaEmpleados.clear()
        self.listaEmpleados.setColumnCount(23)
        self.listaEmpleados.setHorizontalHeaderLabels(['Id', 'Cédula', 'Nombres', 'Apellidos', 'Fecha Nacimiento','Edad', '# Aportaciones', 'Dirección 1', 'Dirección 2', 'Teléfono 1', 'Teléfono 2', 'Email', 'Sueldo', 'Dias Laborales','Género', '   Nivel Académico', '# Cuenta', 'Discapacidad', 'Nombre Recomendado', 'Teléfono Recomendado', 'Celular Recomendado', 'Ciudad', 'Foto'])
        datos = self.Paciente.obtenerPacientes()
        self.listaEmpleados.setRowCount(len(datos))
        for i,row in enumerate(datos):
            for j,val in enumerate(row):
                self.listaEmpleados.setItem(i,j,QtWidgets.QTableWidgetItem(str(val)))

    def EditPaciente(self,clicked):
        #fila = clicked.row()
        self.interfaz.nuevoPaciente()
        datos = self.listaEmpleados.selectedItems()
        self.interfaz.viewFormulario.borrarCampos()
        self.interfaz.viewFormulario.txtID.setText(datos[0].text())
        self.interfaz.viewFormulario.txtCedula.setText(datos[1].text())
        self.interfaz.viewFormulario.txtNombres.setText(datos[2].text())
        self.interfaz.viewFormulario.txtApellidos.setText(datos[3].text())
        self.interfaz.viewFormulario.txtFecha.setDate(datetime.datetime.strptime(datos[4].text(), "%d/%m/%Y"))
        self.interfaz.viewFormulario.txtEdad.setValue(int(datos[5].text()))
        self.interfaz.viewFormulario.txtAport.setValue(int(datos[6].text()))
        self.interfaz.viewFormulario.txtDireccion1.setText(datos[7].text())
        self.interfaz.viewFormulario.txtDireccion2.setText(datos[8].text())
        self.interfaz.viewFormulario.txtTelefono1.setText(datos[9].text())
        self.interfaz.viewFormulario.txtTelefono2.setText(datos[10].text())
        self.interfaz.viewFormulario.txtCorreo.setText(datos[11].text())
        self.interfaz.viewFormulario.txtSueldo.setValue(float(datos[12].text()))
        self.interfaz.viewFormulario.txtDias.setValue(int(datos[13].text()))
        index1 = self.interfaz.viewFormulario.cbxSexo.findText(datos[14].text(), QtCore.Qt.MatchFixedString)
        if index1 >= 0:
            self.interfaz.viewFormulario.cbxSexo.setCurrentIndex(index1)
        index2 = self.interfaz.viewFormulario.cbxNivel.findText(datos[15].text(), QtCore.Qt.MatchFixedString)
        if index2 >= 0:
            self.interfaz.viewFormulario.cbxNivel.setCurrentIndex(index2)
        self.interfaz.viewFormulario.txtCuenta.setText(datos[16].text())
        index3 = self.interfaz.viewFormulario.cbxDiscapacidad.findText(datos[17].text(), QtCore.Qt.MatchFixedString)
        if index3 >= 0:
            self.interfaz.viewFormulario.cbxDiscapacidad.setCurrentIndex(index3)
        self.interfaz.viewFormulario.txtNombreRecom.setText(datos[18].text())
        self.interfaz.viewFormulario.txtTelefonoRecom.setText(datos[19].text())
        self.interfaz.viewFormulario.txtCelularRecom.setText(datos[20].text())
        self.interfaz.viewFormulario.txtCiudad.setText(datos[21].text())
        self.interfaz.viewFormulario.verImagen.setPixmap(QtGui.QPixmap(str(datos[22].text())))
        self.interfaz.viewFormulario.btnGuardar.setText("Modificar")
        self.interfaz.viewFormulario.fotoActual = str(datos[22].text())
        self.interfaz.viewFormulario.btnLimpiar.setEnabled(False)

    def dropPaciente(self):
        datos = self.listaEmpleados.selectedItems()
        if len(datos) <= 0:
            QtWidgets.QMessageBox.information(self, 'Información', 'Seleccione el usuario que desea eliminar', QtWidgets.QMessageBox.Ok)
        else:
            confirmar = QtWidgets.QMessageBox.question(self, "Información", "¿Seguro que desea eliminar los datos de este Paciente?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
            if confirmar == QtWidgets.QMessageBox.Yes:
                QtWidgets.QMessageBox.information(self, 'Información', self.Paciente.dropPaciente(datos[0].text()), QtWidgets.QMessageBox.Ok)
                self.RellenarTabla()

    def Filtrar(self):
        item = self.cbxBusq.currentText()
        self.dato = self.txtBusq.text()
        self.listaEmpleados.clear()
        self.listaEmpleados.setColumnCount(23)
        self.listaEmpleados.setHorizontalHeaderLabels(['Id', 'Cédula', 'Nombres', 'Apellidos', 'Fecha Nacimiento','Edad', '# Aportaciones', 'Dirección 1', 'Dirección 2', 'Teléfono 1', 'Teléfono 2', 'Email', 'Sueldo', 'Dias Laborales','Género', '   Nivel Académico', '# Cuenta', 'Discapacidad', 'Nombre Recomendado', 'Teléfono Recomendado', 'Celular Recomendado', 'Ciudad', 'Foto'])
        if self.dato != '':
            if item == 'Cédula':
                datos = self.Paciente.buscarPacientePorCedula(self.dato)
            elif item == 'Apellidos':
                datos = self.Paciente.buscarPacientePorApellidos(self.dato)
            elif item == 'Nombres':
                datos = self.Paciente.buscarPacientePorNombres(self.dato)
            elif item == 'Ciudad':
                datos = self.Paciente.buscarPacientePorCiudad(self.dato)
        else:
            datos = self.Paciente.obtenerPacientes()
        self.listaEmpleados.setRowCount(len(datos))
        for i,row in enumerate(datos):
            for j,val in enumerate(row):
                self.listaEmpleados.setItem(i,j,QtWidgets.QTableWidgetItem(str(val)))