import sys
import os
from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,QFileDialog,
    QVBoxLayout, QDialog,QTextEdit,QDoubleSpinBox,QSpinBox)
from PySide6.QtCore import QObject, Slot
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, QmlElement
from PySide6.QtQuickControls2 import QQuickStyle

class PlatoUI(QDialog):

    def __init__(self, parent=None):
        super(PlatoUI, self).__init__(parent)
        self.loadVideoPathButton = QPushButton("Load Video")
        self.generateButton = QPushButton("Generate")
        self.feedback = QTextEdit("...")
        self.feedback.setReadOnly(True)
        self.plato = None
        self.log=""

        self.work_files_widgets = []

        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.feedback)
        self.setLayout(self.layout)

    
    def connect(self,_plato_instance):
        
        self.plato = _plato_instance
        self.send_feedback(self.plato.get_user())

    def load_work_files(self):
        work_files = self.plato.get_work_files()
        for wf in work_files : 
            work_file_widget =  Leaf(wf.path,)

            self.layout.addWidget(work_file_widget)



    def send_feedback(self,_message,_overwrite=False):
        print(_message)
        if _overwrite:
            self.log = _message
        else:
            self.log+="<br>"+_message
        self.feedback.setHtml(self.log)

