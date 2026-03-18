#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 16:01:25 2026

@author: samahbouzidi
"""

import sys
# Classe principale pour l'application PyQt5
from PyQt5.QtWidgets import QApplication,QStackedWidget,QVBoxLayout,QWidget
# Import de la fenêtre principale de l'application
from View.start_view import StartView
from View.quiz_view import QuizView
from View.result_view import ResultView

from Controller.quiz_controller import QuizController
from Model.quiz_model import QuizModel

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        
        self.start_view = StartView()
        self.quiz_view = QuizView()
        self.result_view = ResultView()
        
        
        self.stack.addWidget(self.start_view)
        self.stack.addWidget(self.quiz_view)
        self.stack.addWidget(self.result_view)
        
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        
        



app = QApplication(sys.argv)  # Crée l'application
app.setStyle("Fusion")
with open("Resources/style.qss", "r") as file:
    app.setStyleSheet(file.read())
window = MainWindow() # Crée la fenêtre
model=QuizModel()
controller=QuizController(model, window)
window.show()  # Affiche la fenêtre
sys.exit(app.exec_())  # Lance la boucle de l'application et quitte proprement