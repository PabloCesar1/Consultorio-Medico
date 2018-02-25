from PyQt5 import uic, QtWidgets, QtGui, QtCore #importamos uic y QtWidgets desde el modulo PyQt5
import sys
import qdarkstyle # Descargado
import cv2 # Descargado opencv-python
from random import randint
sys.path.append('Datos') 
from Paciente import *
qtFormulario = 'diseno/formulario.ui'
Ui_Formulario, QtBaseClass4 = uic.loadUiType(qtFormulario)
class viewFormPaciente(QtWidgets.QMainWindow, Ui_Formulario):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_Formulario.__init__(self) 
		self.setupUi(self)
		self.btnGuardar.clicked.connect(self.Registrar)
		self.btnLimpiar.clicked.connect(self.borrarCampos)
		self.btnBuscarImg.clicked.connect(self.buscarImagen)
		self.fname = 'Ninguna'

	def Registrar(self):
		if self.selecciona:
			self.guardarImagen()
		paciente = Paciente(self.txtID.text(),self.txtCedula.text(),str(self.txtNombres.text()),
			str(self.txtApellidos.text()),str(self.txtFecha.text()),self.txtEdad.text(),self.txtAport.text(),
			str(self.txtDireccion1.text()),str(self.txtDireccion2.text()),str(self.txtTelefono1.text()),
			str(self.txtTelefono2.text()),str(self.txtCorreo.text()),self.txtSueldo.text().replace(",","."),
			self.txtDias.text(),str(self.cbxSexo.currentText()),str(self.cbxNivel.currentText()),
			str(self.txtCuenta.text()),str(self.cbxDiscapacidad.currentText()),str(self.txtNombreRecom.text()),
			str(self.txtTelefonoRecom.text()),str(self.txtCelularRecom.text()),str(self.txtCiudad.text()),self.fname)
		if self.btnGuardar.text() == "Guardar":
			QtWidgets.QMessageBox.information(self, 'Informacion', paciente.RegistrarPaciente(), QtWidgets.QMessageBox.Ok)
		elif self.btnGuardar.text() == "Modificar":
			QtWidgets.QMessageBox.information(self, 'Informacion', paciente.UpdatePaciente(), QtWidgets.QMessageBox.Ok)

	def borrarCampos(self):
		"""Este metodo nos permite vaciar los campos del formulario de registro"""
		self.txtID.setText("")
		self.txtCedula.setText("")
		self.txtNombres.setText("")
		self.txtApellidos.setText("")
		self.txtEdad.setValue(1)
		self.txtAport.setValue(0)
		self.txtDireccion1.setText("")
		self.txtDireccion2.setText("")
		self.txtTelefono1.setText("")
		self.txtTelefono2.setText("")
		self.txtCorreo.setText("")
		self.txtSueldo.setValue(float(0))
		self.txtDias.setValue(0)
		self.cbxSexo.setCurrentIndex(0)
		self.cbxNivel.setCurrentIndex(0)
		self.txtCuenta.setText("")
		self.cbxDiscapacidad.setCurrentIndex(0)
		self.txtNombreRecom.setText("")
		self.txtTelefonoRecom.setText("")
		self.txtCelularRecom.setText("")
		self.txtCiudad.setText("")
		self.btnLimpiar.setEnabled(True)
		self.verImagen.setPixmap(QtGui.QPixmap(''))
		self.selecciona = False
		self.fname = 'Ninguna'

	def buscarImagen(self):
		"""Este metodo nos permite buscar una imagen en nuestro equipo"""
		fname, filter = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', 'C:\\', 'Image Files (*.jpg)')
		if fname:
			self.selecciona = True
			self.cargarImagen(fname)
		else:
			print('Imagen inválida')
			#QtWidgets.QMessageBox.information(self, 'Informacion', 'Imagen inválida\n solo se aceptan imagenes jpg', QtWidgets.QMessageBox.Ok)
			self.selecciona = False
	def cargarImagen(self, fname):
		"""Este metodo nos permite cargar la imagen seleccionada
			fname representa al nombre del archivo
		"""
		self.image = cv2.imread(fname, cv2.IMREAD_COLOR)
		self.mostrarImagen()
	def mostrarImagen(self):
		"""Este metodo nos permite mostrar en la aplicacion la imagen seleccionada"""
		qformat = QtGui.QImage.Format_Indexed8
		if len(self.image.shape) == 3: # rows[0], cols[1], channels[2]
			if (self.image.shape[2]) == 4:
				qformat = QtGui.QImage.Format_RGB8888
			else:
				qformat = QtGui.QImage.Format_RGB888
		img = QtGui.QImage(self.image, self.image.shape[1], self.image.shape[0], self.image.strides[0], qformat)
		img = img.rgbSwapped()
		self.verImagen.setPixmap(QtGui.QPixmap.fromImage(img))

	def guardarImagen(self):
		"""Este metodo nos permite guardar la imagen en nuestro equipo"""
		self.random = randint(0, 999999999999)
		self.fname = "./fotos/img_"+str(self.random)+'.jpg'
		cv2.imwrite(self.fname, self.image)