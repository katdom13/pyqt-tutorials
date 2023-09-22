# https://www.pythonguis.com/tutorials/pyqt6-plotting-pyqtgraph/

# Plotting with PyQtGraph
# Create custom plots in PyQt6 with PyQtGraph

from PyQt6 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
from random import randint


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)

        self.x = list(range(100))  # 100 time points
        self.y1 = [randint(0,100) for _ in range(100)]  # 100 data points
        self.y2 = [randint(0,100) for _ in range(100)]  # 100 data points

        self.graphWidget.setBackground('w')

        # pen1 = pg.mkPen(color=(255, 0, 0))
        # self.data_line_1 =  self.graphWidget.plot(self.x, self.y1, pen=pen1)

        # pen2 = pg.mkPen(color=(0, 0, 255))
        # self.data_line_2 =  self.graphWidget.plot(self.x, self.y2, pen=pen2)

        self.data_line_1 = self.plot(self.x, self.y1, "numnum1", "red")
        self.data_line_2 = self.plot(self.x, self.y2, "numnum1", "blue")

        self.timer = QtCore.QTimer()
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def plot(self, x, y, plotname, color):
        pen = pg.mkPen(color=color)
        return self.graphWidget.plot(x, y, name=plotname, pen=pen)

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y1 = self.y1[1:]  # Remove the first
        self.y1.append(randint(0,100))  # Add a new random value.

        self.data_line_1.setData(self.x, self.y1)  # Update the data.

        self.y2 = self.y2[1:]  # Remove the first
        self.y2.append(randint(0,100))  # Add a new random value.

        self.data_line_2.setData(self.x, self.y2)  # Update the data.


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec())
