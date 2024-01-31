import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Window")
        self.resize(400, 200)
        #self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground,True)
        #self.setFixedSize(400,300)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)


if __name__ == "__main__":
    app = QApplication([])
    app.setStyle('windows')

    window = MainWindow()
    window.show()
    sys.exit(app.exec()) # main loop