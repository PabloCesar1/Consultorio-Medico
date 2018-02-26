from PyQt5 import uic, QtWidgets, QtGui, QtCore, Qt #importamos uic y QtWidgets desde el modulo PyQt5

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