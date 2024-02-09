import sys
from random import randint
import math
import numpy as np
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction
import pyqtgraph

from package.mainwindow import MainWindow

QApplication.setApplicationName('My Program')
QApplication.setApplicationVersion('0.1')
name = QApplication.applicationName()
version = QApplication.applicationVersion()


PI = 3.1412654
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
        #self.setBackground("#FFFFFF")
        self.xvalues = np.arange(-2*PI,2*PI,0.1)
        self.function = [x**3 for x in self.xvalues]
        self.data = self.plot(self.xvalues,self.function, pen=pyqtgraph.mkPen("b", width=5))
        self.plotItem.setTitle("Hello there")
        self.plotItem.showGrid(x=True,y=True)
        self.plotItem.showAxes(True)

        # Setup a timer to trigger the redraw by calling update_plot.
        self.timer = QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update)
        self.timer.start()

    def update(self) -> None:
        """Update plot"""
        self.data.clear()
        self.data = self.plot(self.xvalues,self.function)

class Menu(QWidget):
    def __init__(self, parent) -> None:
        super().__init__(parent)

        file_action = QAction("Your button", parent)

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

        file_menu = parent.menubar.addMenu("File")


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
    app.setStyle('fusion')
    app.setStyleSheet(stylesheet)
    window.show()
    app.exec()
