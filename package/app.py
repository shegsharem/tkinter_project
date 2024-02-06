import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit
from package.mainwindow import MainWindow

QApplication.setApplicationName('My Program')
QApplication.setApplicationVersion('0.1')
name = QApplication.applicationName()
version = QApplication.applicationVersion()

stylesheet = """
    QLineEdit{
        font-family: JetBrainsMono Nerd Font;
        font-size: 16px;
    }
    QLineEdit:focus{
        background-color: #161b22;
    }
"""
app_style = """
{background-color: #21262d}
"""

class Menu(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit)

        self.input = QLineEdit()
        self.input.setPlaceholderText("Title")
        self.input.setStyleSheet(stylesheet)
        self.input_text = ''
        self.input.returnPressed.connect(self.submit)

        self.textbox = QTextEdit()

        # Widget layout setup
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(submit_button)
        hbox.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        grid = QGridLayout()
        grid.addWidget(self.input,0,0)
        grid.addWidget(self.textbox,1,0)
        grid.addLayout(vbox,2,0)

        self.setLayout(grid)

        # Set widget as centered.
        parent.setCentralWidget(self)

    def submit(self):
        print(self.input.text())
    
    def cancel(self):
        sys.exit()

def run() -> None:
    """Run app"""
    app = QApplication(sys.argv)
    #app.setStyle('fusion')
    window = MainWindow()
    Menu(window)

    window.show()
    app.exec()
