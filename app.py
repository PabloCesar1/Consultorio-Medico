"""Aplicación de Registro de Estudiantes
Creado el 25 de Enero de 2018
@author: Pablo España B.
"""

from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt #importamos uic y QtWidgets desde el modulo PyQt5
import sys
from Connection import Connection
from guiPaciente import *
from guiCitas import *

qtCreatorFile = "menu.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) # usammos loadUiType para cargar el diseño de qt creator

#------------------------------------------  QCalendarWidget QWidget { alternate-background-color: rgb(128, 128, 128); }
class Estudiante(QtWidgets.QMainWindow, Ui_MainWindow):  # Creamos nuestra clase con sus parametros (QtWidgets.QMainWindow y el diseño de qt creator
	"""Este clase contiene los metodos para el manejo de registro de estudiantes"""
	def __init__(self):             # Metodos init para iniciar la aplicacion
		"""Metodo constructor de la clase"""
		QtWidgets.QMainWindow.__init__(self) # Preparamos una ventana principal
		Ui_MainWindow.__init__(self) # Iniciar el diseño de qt creator
		self.setupUi(self)  # Inicializamos la configuracion de la interfaz
		self.setWindowTitle(u"Citas Médicas")
		self.viewPaciente = viewPaciente() #Se llama a viewPaciente de guiPaciente
		self.viewCitas = viewCitas() #Se a viewCitas de guiCitas
		self.menu1.clicked.connect(self.mostrarPaciente)
		self.menu3.clicked.connect(self.citasMedicas)
		self.citasMedicas()

	def mostrarPaciente(self):
		objetos = (self.contenidoPrincipal.itemAt(i).widget() for i in range(self.contenidoPrincipal.count())) 
		crearPaciente = True
		for i in objetos:
			if i ==  self.viewPaciente.contenidoPaciente:
				crearPaciente = False
			i.hide()
		if crearPaciente:
			self.contenidoPrincipal.addWidget(self.viewPaciente.contenidoPaciente)
			print("creando vista Paciente")
		self.viewPaciente.contenidoPaciente.show()

	def citasMedicas(self):
		objetos = (self.contenidoPrincipal.itemAt(i).widget() for i in range(self.contenidoPrincipal.count())) 
		crearCitas = True
		for i in objetos:
			if i ==  self.viewCitas.contenidoCitas:
				crearCitas = False
			i.hide()
		if crearCitas:
			self.contenidoPrincipal.addWidget(self.viewCitas.contenidoCitas)
		self.viewCitas.contenidoCitas.show()

if __name__ == "__main__":
	app =  QtWidgets.QApplication(sys.argv)
	#app.setStyle(QtWidgets.QStyleFactory.create('Fusion')) # <- Choose the style
	myStyle = MyProxyStyle('Fusion')    # The proxy style should be based on an existing style,
	# like 'Windows', 'Motif', 'Plastique', 'Fusion', ...
	app.setStyle(myStyle)
	#dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
	#app.setStyleSheet(dark_stylesheet)
	window = Estudiante()
	window.show()
	notificacion = notificacion()
	notificacion.notificar(app)
	sys.exit(app.exec_())