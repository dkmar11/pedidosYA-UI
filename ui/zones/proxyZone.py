from PySide6.QtWidgets import QHBoxLayout, QVBoxLayout, QLabel, QLineEdit


class ProxyZone:
	def __init__(self):
		self.ipInput = QLineEdit()
		self.portInput = QLineEdit()

	def setupProxyZone(self, layout):
		proxyLayoutV = QVBoxLayout()
		title = QLabel("Configuracion proxy:")
		proxyLayoutV.addWidget(title)
		proxyLayoutH = QHBoxLayout()
		proxyLayoutH.addWidget(QLabel("IP:"))
		proxyLayoutH.addWidget(self.ipInput)
		proxyLayoutH.addWidget(QLabel("Puerto:"))
		proxyLayoutH.addWidget(self.portInput)
		proxyLayoutV.addLayout(proxyLayoutH)

		layout.addLayout(proxyLayoutV)
