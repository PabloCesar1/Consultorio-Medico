from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt #importamos uic y QtWidgets desde el modulo PyQt5
import sys
import datetime
# Importacion de modulos de  datos
sys.path.append('Datos')
from dCitas import *
# Importacion de modulos de vistas
from guiListadoCitas import listadoCitas
from guiNotificacion import notificacion

qtCitas = "diseno/calendarioCitas.ui" # Archivo con los componentes gráficos
Ui_MainWindowCitas, QtBaseClassCitas = uic.loadUiType(qtCitas) # carga del archivo

class calendarioCitas(QtWidgets.QMainWindow, Ui_MainWindowCitas):  # Creamos nuestra clase con sus parametros (QtWidgets.QMainWindow y el diseño de qt creator
	"""Este clase contiene los metodos para el manejo de registro de estudiantes"""
	def __init__(self):             # Metodos init para iniciar la aplicacion
		"""Metodo constructor de la clase"""
		QtWidgets.QMainWindow.__init__(self) # Preparamos una ventana principal
		Ui_MainWindowCitas.__init__(self) # Iniciar el diseño de qt creator
		self.setupUi(self)  # Inicializamos la configuracion de la interfaz
		self.setWindowTitle(u"Citas Médicas")
		self.calendario.clicked[QtCore.QDate].connect(self.mostrarFecha)
		self.calendario.activated[QtCore.QDate].connect(self.mostrarCitas)
		self.format = QtGui.QTextCharFormat()
		self.format.setBackground(QtCore.Qt.green)
		self.citasPorMes()
		self.numeroCitasDiaria()

	def mostrarFecha(self):
		self.date = self.calendario.selectedDate()
		self.listadoCitas = listadoCitas(self.date)

	def mostrarCitas(self):
		self.listadoCitas.show()

	def citasPorMes(self): # Colorea la fecha en la que hay citas médicas
		c = dCita() # Instancia de la clase dCita (de datos)
		result = c.consultaCitas() # Obtengo el resultado de la consulta
		for row in result: # Por cada fila en el resultado obtenido se pintaran de verde las fechas en que hayan citas 
			self.calendario.setDateTextFormat(datetime.datetime.strptime(row[4], "%d/%m/%Y"), self.format)

	def numeroCitasDiaria(self):
		c = dCita() # Instancia de la clase dCita (de datos)
		result = c.numeroCitasDiarias() # Obtengo el resultado de la consulta
		self.lblNumeroCitas.setText(str(len(result[0]))) # muestro en el label la cantidad de citas diarias
		self.lblFechaActual.setText('Fecha: \n'+result[1]) # muestro en el label la fecha actual
		n = notificacion() # Instancia de la clase notificación
		n.informacion(len(result[0])) # Envía la cantidad de citas diarias que se mostrará en la notificación


class MyProxyStyle(QtWidgets.QProxyStyle):
	# Soporte para pantallas 4k
	pass
	def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None):

		if QStyle_PixelMetric == QtWidgets.QStyle.PM_SmallIconSize:
			return 40
		else:
			return QtWidgets.QProxyStyle.pixelMetric(self, QStyle_PixelMetric, option, widget)