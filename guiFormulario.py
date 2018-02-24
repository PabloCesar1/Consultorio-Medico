from PyQt5 import uic, QtWidgets, QtGui, QtCore #importamos uic y QtWidgets desde el modulo PyQt5
import sys

qtFormulario = 'formulario.ui'
Ui_Formulario, QtBaseClass4 = uic.loadUiType(qtFormulario)
class viewFormPaciente(QtWidgets.QMainWindow, Ui_Formulario):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Formulario.__init__(self) 
        self.setupUi(self)
    """    
    def LimpiarFormulario(self)
    	formulario
    """