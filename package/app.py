import sys
from random import randint
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QHBoxLayout, QVBoxLayout, QTextEdit, QMenuBar, QLabel
from PyQt6.QtCore import Qt, QTimer
import pyqtgraph

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
        font-weight:bold;
        font-size: 18px;
        padding: 5px;
        border-radius: 10px;
        margin:2px;
    }

    QPushButton{
        font-family: JetBrainsMono Nerd Font, Consolas;
    }

    QMenuBar{
        font-family: JetBrainsMono Nerd Font, Consolas;
    }

    QLabel{
        font-family: JetBrainsMono Nerd Font, Consolas;
        font-weight:bold;
        font-size: 18px;
        margin:2px;
    }

"""

class Plot(pyqtgraph.PlotWidget):
    """PyQt6 Widget for plotting graphs"""
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setBackground("#FFFFFF")
        self.time = [1,2,3,4,5,6,7]
        self.temperature = [29,30,30,10,20,12,34]
        self.data = self.plot(self.time,self.temperature)

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update)
        self.timer.start()

    def update(self) -> None:
        """Update plot"""
        self.data.clear()
        self.temperature = [randint(15,35) for i in range(7)]
        self.data = self.plot(self.time,self.temperature)

class Menu(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        cancel_button = QPushButton("Cancel")
        cancel_button.clicked.connect(self.cancel)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit)

        self.title = QLabel()
        self.title.setText("My Graph")

        self.input = QLineEdit()
        self.input.setStyleSheet(stylesheet)
        self.input_text = ''
        self.input.returnPressed.connect(self.changeTitle)

        self.plot = Plot()

        # Widget layout setup
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(submit_button)
        hbox.addWidget(cancel_button)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)

        grid = QGridLayout()
        grid.addWidget(self.title,0,0)
        grid.addWidget(self.input,1,0)
        grid.addWidget(self.plot,2,0)
        grid.addLayout(vbox,3,0)

        self.input.hide()

        self.setLayout(grid)

        # Set widget as centered.
        parent.setCentralWidget(self)

    def submit(self):
        self.title.hide()
        self.input.show()
        self.input.setText(self.title.text())
        self.input.selectAll()
        self.input.setFocus()
        print(self.input.text())
    
    def cancel(self):
        sys.exit()

    def changeTitle(self):
        self.input.hide()
        self.title.setText(self.input.text())
        self.title.show()

def run() -> None:
    """Run app"""
    app = QApplication(sys.argv)
    window = MainWindow()
    Menu(window)
    #app.setStyle('fusion')
    app.setStyleSheet(stylesheet)
    window.show()
    app.exec()
