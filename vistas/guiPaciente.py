from PyQt5 import uic, QtWidgets, QtGui, QtCore #importamos uic y QtWidgets desde el modulo PyQt5
import sys
import psycopg2
sys.path.append('Datos') 
from Paciente import *

qtPaciente = 'diseno/paciente.ui'
Ui_Paciente, QtBaseClass4 = uic.loadUiType(qtPaciente)
class viewPaciente(QtWidgets.QMainWindow, Ui_Paciente):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Paciente.__init__(self) 
        self.setupUi(self)
        self.Paciente = Paciente()
        self.RellenarTabla()

    def RellenarTabla(self):
        self.listaEmpleados.clear()
        self.listaEmpleados.setColumnCount(23)
        self.listaEmpleados.setHorizontalHeaderLabels(['Id', 'Cédula', 'Nombres', 'Apellidos', 'Fecha Nacimiento','Edad', '# Aportaciones', 'Dirección 1', 'Dirección 2', 'Teléfono 1', 'Teléfono 2', 'Email', 'Sueldo', 'Dias Laborales','Género', '   Nivel Académico', '# Cuenta', 'Discapacidad', 'Nombre Recomendado', 'Teléfono Recomendado', 'Celular Recomendado', 'Ciudad', 'Foto'])
        datos = self.Paciente.obtenerPacientes()
        self.listaEmpleados.setRowCount(len(datos))
        for i,row in enumerate(datos):
            for j,val in enumerate(row):
                self.listaEmpleados.setItem(i,j,QtWidgets.QTableWidgetItem(str(val)))
        
