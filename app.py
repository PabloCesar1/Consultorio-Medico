"""Aplicación de Registro de Estudiantes
Creado el 25 de Enero de 2018
@author: Pablo España B.
"""

from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt #importamos uic y QtWidgets desde el modulo PyQt5
import sys
from Connection import Connection
sys.path.append('vistas') 
from guiPaciente import *
from guiCitas import *
from guiFormulario import *
qtCreatorFile = "diseno/menu.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) # usammos loadUiType para cargar el diseño de qt creator

#-------------------------------------------------------------------------------------------------
class Estudiante(QtWidgets.QMainWindow, Ui_MainWindow):  # Creamos nuestra clase con sus parametros (QtWidgets.QMainWindow y el diseño de qt creator
	"""Este clase contiene los metodos para el manejo de registro de estudiantes"""
	def __init__(self):             # Metodos init para iniciar la aplicacion
		"""Metodo constructor de la clase"""
		QtWidgets.QMainWindow.__init__(self) # Preparamos una ventana principal
		Ui_MainWindow.__init__(self) # Iniciar el diseño de qt creator
		self.setupUi(self)  # Inicializamos la configuracion de la interfaz
		self.setWindowTitle(u"Citas Médicas")
		self.viewPaciente = viewPaciente(self) #Se llama a viewPaciente de guiPaciente
		self.viewCitas = viewCitas() #Se a viewCitas de guiCitas
		self.viewFormulario = viewFormPaciente()
		self.menu1.clicked.connect(self.mostrarPaciente)
		self.menu3.clicked.connect(self.citasMedicas)
		# se le asigna el evento al boton "nuevo" de la vista paciente
		self.viewPaciente.btnNuevo.clicked.connect(self.nuevoPaciente)
		#se le asigna el evento al boton "regresar" de la vista del formulario
		self.viewFormulario.btnRegresar.clicked.connect(self.mostrarPaciente)
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
		self.viewPaciente.RellenarTabla()
		self.menu1.setStyleSheet("background-color:#0cc597;");
		self.menu3.setStyleSheet("background-color:#2c333e;");

	def citasMedicas(self):
		objetos = (self.contenidoPrincipal.itemAt(i).widget() for i in range(self.contenidoPrincipal.count())) 
		crearCitas = True
		for i in objetos:
			if i ==  self.viewCitas.contenidoCitas:
				crearCitas = False
			i.hide()
		if crearCitas:
			self.contenidoPrincipal.addWidget(self.viewCitas.contenidoCitas)
			print("creando vista Citas")
		self.viewCitas.contenidoCitas.show()
		self.menu3.setStyleSheet("background-color:#0cc597;");
		self.menu1.setStyleSheet("background-color:#2c333e;");

	def nuevoPaciente(self):
		objetos = (self.contenidoPrincipal.itemAt(i).widget() for i in range(self.contenidoPrincipal.count())) 
		crearForm = True
		for i in objetos:
			if i ==  self.viewFormulario.centralwidget:
				crearForm = False
			i.hide()
		if crearForm:
			self.contenidoPrincipal.addWidget(self.viewFormulario.centralwidget)
			print("creando vista FormPaciente")
		self.viewFormulario.centralwidget.show()
		self.viewFormulario.borrarCampos()
		self.viewFormulario.btnGuardar.setText("Guardar")

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