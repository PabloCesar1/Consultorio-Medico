from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt #importamos uic y QtWidgets desde el modulo PyQt5
import sys, os
# Importacion de modulos de  datos
sys.path.append('Datos')
from dCitas import *
# Importacion de modulos de vistas
from guiFormularioCita import Cita as frmCita

qtDia = 'diseno/listadoCitas.ui' # Archivo con los componentes gráficos
Ui_Dia, QtBaseClass2 = uic.loadUiType(qtDia)  # carga del archivo

class listadoCitas(QtWidgets.QMainWindow, Ui_Dia):
	
	def __init__(self, date):
		self.date = date
		QtWidgets.QMainWindow.__init__(self)
		Ui_Dia.__init__(self) # Iniciar el diseño de qt creator
		self.setupUi(self)
		self.setWindowTitle("Citas Médicas")
		self.btnNuevo.clicked.connect(self.nuevaCita)
		self.lblDia.setText(self.date.toString())
		self.citas.cellClicked.connect(self.obtenerHora)
		self.citasPorDia()

	def citasPorDia(self):
		c = dCita() # Instancia de la clase dCita (de datos)
		result = c.consultaCitasPorDias(self.date) # Obtengo el resultado de la consulta
		for row in result: # Por cada fila en el resultado
			hora = row[5]
			for index in range(25): # Comparar la hora de la base de datos con la de la fila
				horaFila = self.citas.verticalHeaderItem(index).text() # Horas de la tabla (de 00:00 a 24:00)
				if horaFila == hora: # si la hora de la fila es igual al del resultado de la consulta
					#--------------Mostrar datos en tabla-----------
					self.citas.setItem(index, 0, QtWidgets.QTableWidgetItem(row[1]))
					self.citas.item(index, 0).setBackground(QtCore.Qt.green) # Cambiar color de la columna a verde
					self.citas.setItem(index, 1, QtWidgets.QTableWidgetItem(row[2]))
					self.citas.item(index, 1).setBackground(QtCore.Qt.green) # Cambiar color de la columna a verde
					self.citas.setItem(index, 2, QtWidgets.QTableWidgetItem(row[3]))
					self.citas.item(index, 2).setBackground(QtCore.Qt.green) # Cambiar color de la columna a verde

	def obtenerHora(self):
		indexes = self.citas.selectionModel().selectedRows()
		self.hora = None
		for index in sorted(indexes):
			self.hora = self.citas.verticalHeaderItem(index.row()).text()
			print(self.hora)

	def nuevaCita(self):
		if  hasattr(self, 'hora'):
			self.frmCita = frmCita(self.date, self.hora) # Instancia de la clase
			self.frmCita.show()
		else:
			QtWidgets.QMessageBox.information(self, 'Informacion', 'Por favor Seleccione la hora de la cita', QtWidgets.QMessageBox.Ok)