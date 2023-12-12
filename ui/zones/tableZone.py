from PySide6.QtWidgets import QHBoxLayout, QPushButton, QTableWidget

class TableZone:
  def __init__(self):
    self.addButton = QPushButton("Agregar")
    self.deleteButton = QPushButton("Eliminar")
    self.table = QTableWidget()

  def setupTableZone(self, layout):
    buttonsLayout = QHBoxLayout()
    buttonsLayout.addWidget(self.addButton)
    buttonsLayout.addWidget(self.deleteButton)

    self.table.setColumnCount(5)
    self.table.setHorizontalHeaderLabels(["Hora inicio", "Hora fin", "Hora min", "Zona", "Dia sig?"])
    
    layout.addLayout(buttonsLayout)
    layout.addWidget(self.table)
