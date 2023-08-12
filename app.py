from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QPushButton, QMainWindow

# For accessing command line arguments
import sys


# QMainWindow is a pre-made widget which provides a lot of standard window features
# The best approach is to subclass it and include any setup in the __init__ block
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My app")
        button = QPushButton("Press me")

        # Sets a fixed size for the window
        self.setFixedSize(QSize(400, 300))

        # Set the central widget of the window
        self.setCentralWidget(button)


# A QApplication instance is required per application
app = QApplication(sys.argv)

# Any widget can be a window
# window = QWidget()
# window = QPushButton("Push Me")

window = MainWindow()

# Windows are hidden by default
window.show()

# Start the loop
app.exec()
