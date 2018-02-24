from PyQt5 import uic, QtWidgets, QtGui, QtCore #importamos uic y QtWidgets desde el modulo PyQt5
import sys
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

    def Registrar(self):
    	paciente = Paciente(self.txtID.text(),self.txtCedula.text(),str(self.txtNombres.text()),
    		str(self.txtApellidos.text()),str(self.txtFecha.text()),self.txtEdad.text(),self.txtAport.text(),
    		str(self.txtDireccion1.text()),str(self.txtDireccion2.text()),str(self.txtTelefono1.text()),
    		str(self.txtTelefono2.text()),str(self.txtCorreo.text()),self.txtSueldo.text().replace(",","."),
    		self.txtDias.text(),str(self.cbxSexo.currentText()),str(self.cbxNivel.currentText()),
    		str(self.txtCuenta.text()),str(self.cbxDiscapacidad.currentText()),str(self.txtNombreRecom.text()),
    		str(self.txtTelefonoRecom.text()),str(self.txtCelularRecom.text()),str(self.txtCiudad.text()),'Ninguna')
    	QtWidgets.QMessageBox.information(self, 'Informacion', paciente.RegistrarPaciente(), QtWidgets.QMessageBox.Ok)

    """    
    def LimpiarFormulario(self)
    	formulario
    """