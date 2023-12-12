from PySide6.QtWidgets import QApplication
from ui.mainView import MainView

def main():
    app = QApplication([])
    window = MainView()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
