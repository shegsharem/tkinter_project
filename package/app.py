import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit, QMenuBar
from PyQt6.QtCore import Qt
from package.mainwindow import MainWindow

QApplication.setApplicationName('My Program')
QApplication.setApplicationVersion('0.1')
name = QApplication.applicationName()
version = QApplication.applicationVersion()

stylesheet = """
    QMainWindow:separator {
        background: #3C3C3E;
    }
    QLineEdit{
        font-family: JetBrainsMono Nerd Font, Consolas;
        font-size: 16px;
        padding: 5px;
        border-radius: 10px;
    }

    QPushButton{
        font-family: JetBrainsMono Nerd Font, Consolas;
    }

    QMenuBar{
        font-family: JetBrainsMono Nerd Font, Consolas;
    }

"""

class Menu(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit)

        menubar = QMenuBar(parent)
        menubar.addMenu("File")
        menubar.addMenu("Edit")

        self.input = QLineEdit()
        self.input.setPlaceholderText("Title")
        self.input.setStyleSheet(stylesheet)
        self.input_text = ''
        self.input.returnPressed.connect(self.submit)

        self.textbox = QTextEdit()

        menubarbox = QHBoxLayout()
        menubarbox.addWidget(menubar)

        # Widget layout setup
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(submit_button)
        hbox.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        grid = QGridLayout()
        grid.addLayout(menubarbox,0,0)
        grid.addWidget(self.input,1,0)
        grid.addWidget(self.textbox,2,0)
        grid.addLayout(vbox,3,0)


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
    window = MainWindow()
    Menu(window)
    #app.setStyle('fusion')
    app.setStyleSheet(stylesheet)
    window.show()
    app.exec()
