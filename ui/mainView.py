from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QPushButton
from PySide6.QtCore import QTimer
from logger import logger
from ui.zones.proxyZone import ProxyZone
from ui.zones.loggerZone import LoggerZone
from ui.zones.searchZone import SearchZone
from ui.zones.objectivesZone import ObjectivesZone
from ui.zones.tableZone import TableZone
from ui.utils.tableFunction import addObjective, deleteLastObjective

class MainView(QMainWindow):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("PedidosYa Bot")

		# timer
		self.timer = QTimer(self)
		self.timer_auto_login = QTimer(self)
		self.timer_day_by_day = QTimer(self)
		# main layout
		layout = QVBoxLayout()

		# Zones
		self.SearchZone = SearchZone()
		self.ProxyZone = ProxyZone()
		self.LoggerZone = LoggerZone()
		self.ObjectivesZone = ObjectivesZone()
		self.TableZone = TableZone()

		# setup
		self.ProxyZone.setupProxyZone(layout)
		self.LoggerZone.setupLoggerZone(layout)
		self.SearchZone.setupSearchZone(layout)
		self.ObjectivesZone.setupObjectivesZone(layout)
		self.TableZone.setupTableZone(layout)

		self.save_button = QPushButton("Empezar")
		layout.addWidget(self.save_button)

		# connect
		self.TableZone.addButton.clicked.connect(lambda: addObjective(self.TableZone, self.ObjectivesZone))
		self.TableZone.deleteButton.clicked.connect(lambda: deleteLastObjective(self.TableZone))

		widget = QtWidgets.QWidget()
		widget.setLayout(layout)
		self.setCentralWidget(widget)
