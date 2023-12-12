from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, QSpinBox, QTimeEdit, QComboBox
from PySide6.QtCore import QTime

class LoggerZone:
  def __init__(self):
    self.usernameInput = QLineEdit()
    self.passwordInput = QLineEdit()
  
  def setupLoggerZone(self, layout):
    userLayout = QHBoxLayout()

    userLayout.addWidget(QLabel("Usuario:"))
    userLayout.addWidget(self.usernameInput)
    userLayout.addWidget(QLabel("Contraseña:"))
    self.passwordInput.setEchoMode(QLineEdit.Password)
    userLayout.addWidget(self.passwordInput)

    layout.addWidget(QLabel("Datos de usuario:"))
    layout.addLayout(userLayout)
  