from PySide6.QtWidgets import QHBoxLayout, QLabel,  QTimeEdit, QFormLayout, QSpinBox, QLineEdit, QComboBox
from PySide6.QtCore import QTime


class ObjectivesZone:
  def __init__(self):
    self.startTime = QTimeEdit()
    self.endTime = QTimeEdit()
    self.minHour = QLineEdit()
    self.zone = QComboBox()
    self.nextDay = QComboBox()
    self.refreshTime = QSpinBox()

  def setupObjectivesZone(self, layout):
    objectiveLayout = QFormLayout()

    hoursLayout = QHBoxLayout()
    hoursLayout.addWidget(QLabel("Hora inicio: "))

    self.startTime.setTime(QTime.currentTime())
    hoursLayout.addWidget(self.startTime)

    hoursLayout.addWidget(QLabel(" Hora fin: "))

    self.endTime.setTime(QTime.currentTime())
    hoursLayout.addWidget(self.endTime)

    hoursLayout.addWidget(QLabel(" Hora min: "))

    hoursLayout.addWidget(self.minHour)

    objectiveLayout.addRow(hoursLayout)

    self.zone.addItems(["Zonas principales", "Zona Sur", "Grigota", "Sevilla",  "Equipetrol", "Guapay", "La Alemana", "El bajio",
                      "Pirai", "Norte",  "Santos Dumont", "Fidalga pampa", "Hipermaxi pampa",  "Villa 1° de mayo", "Warnes", "Montero", "Satelite"])
    self.zone.setFixedWidth(180)

    self.zoneRefreshLayout = QHBoxLayout()
    self.zoneRefreshLayout.addWidget(QLabel("Zona:"))
    self.zoneRefreshLayout.addWidget(self.zone)

    self.nextDay.addItems(["No", "Si"])
    self.zoneRefreshLayout.addWidget(QLabel(" Dia sig? "))
    self.zoneRefreshLayout.addWidget(self.nextDay)

    labelRefresh = QLabel(" Refresh:")
    labelRefresh.setFixedWidth(72)
    self.zoneRefreshLayout.addWidget(labelRefresh)

    self.refreshTime.setMinimum(200)
    self.refreshTime.setValue(200)
    self.zoneRefreshLayout.addWidget(self.refreshTime)
    objectiveLayout.addRow(self.zoneRefreshLayout)

    layout.addWidget(QLabel("Objetivos:"))
    layout.addLayout(objectiveLayout)
