from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt #importamos uic y QtWidgets desde el modulo PyQt5
import sys
import datetime
from Connection import Connection
sys.path.append('Datos')
from dCitas import *

qtCitas = "diseno/citas.ui"
qtDia = 'diseno/dia.ui'
qtCita = 'diseno/nueva.ui'

Ui_MainWindowCitas, QtBaseClassCitas = uic.loadUiType(qtCitas)
Ui_Dia, QtBaseClass2 = uic.loadUiType(qtDia)
Ui_Cita, QtBaseClass3 = uic.loadUiType(qtCita)

class viewCitas(QtWidgets.QMainWindow, Ui_MainWindowCitas):  # Creamos nuestra clase con sus parametros (QtWidgets.QMainWindow y el diseño de qt creator
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
		self.infCitas = informacionCitas(self.date)

	def mostrarCitas(self):
		self.infCitas.show()

	
	def citasPorMes(self): # Colorea la fecha en la que hay citas médicas
		c = dCita() # Instancia de la clase dCita (de datos)
		result = c.consultaCitas() # Obtengo el resultado de la consulta
		for row in result: # Por cada fila en el resultado obtenido se pintaran de verde las fechas en que hayan citas 
			self.calendario.setDateTextFormat(datetime.datetime.strptime(row[4], "%d/%m/%Y"), self.format)

	def numeroCitasDiaria(self):
		self.conn = Connection.Connect()
		cursor = self.conn.cursor()
		d = datetime.datetime.now()
		hoy = (str(d.day)+'/'+str(d.month)+'/'+str(d.year))
		cursor.execute("SELECT * FROM citas WHERE fecha =  %s;", [hoy])
		result = cursor.fetchall()
		self.lblNumeroCitas.setText(str(len(result)))
		self.lblFechaActual.setText('Fecha: \n'+hoy)
		cursor.close()
		self.conn.close()
		n = notificacion()
		n.informacion(len(result))

#--------------------------------------------------------------------
class informacionCitas(QtWidgets.QMainWindow, Ui_Dia):
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

	def obtenerHora(self):
		indexes = self.citas.selectionModel().selectedRows()
		self.hora = None
		for index in sorted(indexes):
			self.hora = self.citas.verticalHeaderItem(index.row()).text()
			print(self.hora)

	def nuevaCita(self):
		if  hasattr(self, 'hora'):
			self.cita = Cita(self.date, self.hora) # Instancia de la clase
			self.cita.show()
		else:
			QtWidgets.QMessageBox.information(self, 'Informacion', 'Por favor Seleccione la hora de la cita', QtWidgets.QMessageBox.Ok)

	def citasPorDia(self):
		self.conn = Connection.Connect()
		cursor = self.conn.cursor()
		self.fecha = (str(self.date.day()) +'/'+str(self.date.month()) +'/'+str(self.date.year()))
		cursor.execute("SELECT * FROM citas WHERE fecha =  %s;", [self.fecha])
		result = cursor.fetchall()
		for row in result:
			hora = row[5]
			#------------Comparar la hora de la base de datos con la de la fila--------------
			for index in range(25):
				horaFila = self.citas.verticalHeaderItem(index).text()
				if horaFila == hora:
					#--------------Mostrar datos en tabla-----------
					self.citas.setItem(index, 0, QtWidgets.QTableWidgetItem(row[1]))
					self.citas.item(index, 0).setBackground(QtCore.Qt.green)
					self.citas.setItem(index, 1, QtWidgets.QTableWidgetItem(row[2]))
					self.citas.item(index, 1).setBackground(QtCore.Qt.green)
					self.citas.setItem(index, 2, QtWidgets.QTableWidgetItem(row[3]))
					self.citas.item(index, 2).setBackground(QtCore.Qt.green)

		cursor.close()
		self.conn.close()

#--------------------------------------------------------------------------------------------------
class Cita(QtWidgets.QMainWindow, Ui_Cita):
	def __init__(self, date, hora):
		QtWidgets.QMainWindow.__init__(self)
		Ui_Cita.__init__(self) # Iniciar el diseño de qt creator
		self.setupUi(self)
		self.setWindowTitle("Nueva Cita")
		self.fecha = (str(date.day()) +'/'+str(date.month()) +'/'+str(date.year()))
		self.txtFecha.setDate(datetime.datetime.strptime(self.fecha, "%d/%m/%Y"))
		self.txtHora.setText(hora)
		self.btnGuardar.clicked.connect(self.registrarCita)

	def registrarCita(self):
		paciente = str(self.txtPaciente.text())
		doctor = str(self.txtDoctor.text())
		descripcion = str(self.txtDescripcion.text())
		fecha = str(self.txtFecha.text())
		hora = str(self.txtHora.text())
		descripcion = str(self.txtDescripcion.text())
		c = dCita(None, paciente, doctor, descripcion, fecha, hora)
		QtWidgets.QMessageBox.information(self, 'Informacion', c.registrarCita(), QtWidgets.QMessageBox.Ok)


class notificacion():
	citas = 0
	def informacion(self, numero):
		global citas
		citas = numero
	def notificar(self, app):
		systemtray_icon = Qt.QSystemTrayIcon(Qt.QIcon('/path/to/image'), app)
		systemtray_icon.show()
		if citas == 1:
			systemtray_icon.showMessage('Citas de hoy', 'Tiene '+str(citas)+' cita con un paciente para hoy')
		else:
			systemtray_icon.showMessage('Citas de hoy', 'Tiene '+str(citas)+' citas para el día de hoy')

class MyProxyStyle(QtWidgets.QProxyStyle):
	""" Soporte para pantallas 4k"""
	pass
	def pixelMetric(self, QStyle_PixelMetric, option=None, widget=None):

		if QStyle_PixelMetric == QtWidgets.QStyle.PM_SmallIconSize:
			return 40
		else:
			return QtWidgets.QProxyStyle.pixelMetric(self, QStyle_PixelMetric, option, widget)