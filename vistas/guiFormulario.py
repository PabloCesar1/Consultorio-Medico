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
        self.btnGuardar.setText("Guardar")