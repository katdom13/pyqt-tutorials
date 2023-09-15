# https://www.pythonguis.com/tutorials/pyqt6-first-steps-qt-designer/

# First steps with Qt Designer
# Use Qt Designer's drag and drop interface to design your PyQt6 GUI

import sys
from PyQt6 import QtWidgets, uic

from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)


app = QtWidgets.QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()


# Converting your .ui file to Python
# pyuic6 mainwindow.ui -o MainWindow.py
