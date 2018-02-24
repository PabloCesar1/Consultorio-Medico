from PyQt5 import uic, QtWidgets, QtGui, QtCore #importamos uic y QtWidgets desde el modulo PyQt5
import sys

qtPaciente = 'paciente.ui'
Ui_Paciente, QtBaseClass4 = uic.loadUiType(qtPaciente)
class viewPaciente(QtWidgets.QMainWindow, Ui_Paciente):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_Paciente.__init__(self) 
        self.setupUi(self)
        self.btnLimpiar.clicked.connect(self.limpiar)

    def limpiar(self):
        print('probando')