from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Window")
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        button = QPushButton("Press Here")
        self.setFixedSize(400,300)

        self.setCentralWidget(button)

app = QApplication([])
app.setStyle('windows')

window = MainWindow()
window.show()

app.exec() # main loop