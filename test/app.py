from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor


# Only needed for access to command line arguments
import sys
import os

print("hello")

# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)

class FileBar(QHBoxLayout):
    def __init__(self, _path):
        self.path = _path
        super().__init__()

        label = QLabel(_path)
        button = QPushButton("open")
        self.addWidget(label)
        self.addWidget(button)
        button .pressed.connect(self.open_file)
    def open_file(self):
        os.system(self.path )

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        label = QLabel(" HELLO ")
        label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()

        layout.addLayout(FileBar('D:/1_TRAVAIL/WEB/sandbox/QT/test.txt'))
        layout.addLayout(FileBar('D:/1_TRAVAIL/WEB/sandbox/QT/test.txt'))
        layout.addLayout(FileBar('D:/1_TRAVAIL/WEB/sandbox/QT/test.txt'))
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.setFixedSize(QSize(400, 300))

# Create a Qt widget, which will be our window.
window = MainWindow()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.


#python3 D:/1_TRAVAIL/WEB/sandbox/QT/app.py
