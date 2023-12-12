from PySide6.QtWidgets import QHBoxLayout, QLabel, QDateEdit
from PySide6.QtCore import QDate

class SearchZone():
	def __init__(self):
		self.searchStartDate = QDateEdit()
		self.searchEndDate = QDateEdit()

	def setupSearchZone(self, layout):
		searchLayout = QHBoxLayout()
		searchLayout.addWidget(QLabel("Fecha inicio:"))

		self.searchStartDate.setDate(QDate.currentDate())
		self.searchStartDate.setDisplayFormat("dd/MM/yyyy")
		searchLayout.addWidget(self.searchStartDate)

		searchLayout.addWidget(QLabel("Fecha final:"))
		self.searchEndDate.setDate(QDate.currentDate())
		self.searchEndDate.setDisplayFormat("dd/MM/yyyy")
		searchLayout.addWidget(self.searchEndDate)
		
		layout.addWidget(QLabel("Datos de búsqueda:"))
		layout.addLayout(searchLayout)
