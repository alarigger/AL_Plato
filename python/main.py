import sys
import os
from  model.Plato import Plato
from  view.PlatoUI import PlatoUI
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,QFileDialog,
    QVBoxLayout, QDialog,QTextEdit,QDoubleSpinBox,QSpinBox)


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    PlatoControl = Plato()
    # Create and show the form
    PlatoView = PlatoUI()
    PlatoView.connect(PlatoControl)
    PlatoView.show()
    PlatoView.load_work_files()
    # Run the main Qt loop
    sys.exit(app.exec_())


'''
python D:\1_TRAVAIL\WIP\ALARIGGER\CODING\PYTHON\REPOSITORIES\AL_Plato\python\main.py
'''