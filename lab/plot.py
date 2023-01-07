# importing Qt widgets
from PyQt5.QtWidgets import *
import sys
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("PyQtGraph")
        # setting geometry
        self.setGeometry(100, 100, 600, 500)
        # calling method
        self.UiComponents()
        # showing all the widgets
        self.show()

    # method for components
    def UiComponents(self):

        # creating a widget object
        widget = QWidget()
        # creating a push button object
        btn = QPushButton("Push Button")
        # creating a line edit widget
        text = QLineEdit("Line Edit")
        # creating a check box widget
        check = QCheckBox("Check Box")
        # creating a plot window
        plot = pg.plot()

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0, 100) for _ in range(100)]  # 100 data points
        self.bargraph = pg.BarGraphItem(x=self.x, height=self.y, width=0.6, brush="g")
        plot.addItem(self.bargraph)
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(btn, 0, 0)
        layout.addWidget(text, 1, 0)
        layout.addWidget(check, 3, 0)
        layout.addWidget(plot, 0, 1, 3, 1)
        self.setCentralWidget(widget)

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):
        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.
        self.y = self.y[1:]  # Remove the first
        self.y.append(randint(0, 100))  # Add a new random value.
        self.bargraph.setData(self.x, self.y)  # Update the data.


# create pyqt5 app
App = QApplication(sys.argv)
# create the instance of our Window
window = Window()
# start the app
sys.exit(App.exec())


# class MainWindow(QtWidgets.QMainWindow):
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)

#         self.graphWidget = pg.PlotWidget()
#         self.setCentralWidget(self.graphWidget)

#         self.x = list(range(100))  # 100 time points
#         self.y = [randint(0, 100) for _ in range(100)]  # 100 data points

#         self.graphWidget.setBackground("w")

#         pen = pg.mkPen(color=(255, 0, 0))
#         self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen)

#         self.timer = QtCore.QTimer()
#         self.timer.setInterval(50)
#         self.timer.timeout.connect(self.update_plot_data)
#         self.timer.start()

#     def update_plot_data(self):

#         self.x = self.x[1:]  # Remove the first y element.
#         self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

#         self.y = self.y[1:]  # Remove the first
#         self.y.append(randint(0, 100))  # Add a new random value.

#         self.data_line.setData(self.x, self.y)  # Update the data.
