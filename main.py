import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
    QLabel,
    QStyle,
    QToolButton
)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Window")
        layout = QVBoxLayout()

        widgets = [
            Editor()
        ]

        for widget in widgets:
            layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(layout)


        self.setCentralWidget(widget)


class Editor(QWidget):
    def __init__(self) -> None:
        super().__init__()
        layout = QVBoxLayout()
        self.setLayout(layout)

        button_save = QPushButton("Save")
        button_save.resize(button_save.sizeHint())
        button_save.clicked.connect(self.save)

        button_cancel = QPushButton("Cancel")
        button_cancel.resize(button_cancel.sizeHint())
        button_cancel.clicked.connect(self.save)

        layout.addWidget(button_save,alignment=Qt.AlignmentFlag.AlignTrailing)
        layout.addWidget(button_cancel,alignment=Qt.AlignmentFlag.AlignTrailing)


    
    def save(self) -> None:
        print("clicked")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('windows')

    window = MainWindow()
    window.show()
    sys.exit(app.exec()) # main loop