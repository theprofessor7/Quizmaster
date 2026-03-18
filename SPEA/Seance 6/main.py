#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 16:01:25 2026

@author: samahbouzidi
"""

from PyQt5.QtGui import QIcon

import sys
# Classe principale pour l'application PyQt5
from PyQt5.QtWidgets import QVBoxLayout,QWidget,QApplication,QMainWindow,QStackedWidget

from View.start_view import StartView
from View.quiz_view import QuizView
from View.result_view import ResultView
from PyQt5.QtCore import Qt
from Model.quiz_model import QuizModel
from Controller.quiz_controller import QuizController

class MainWindow(QWidget):

    def __init__(self):

        super().__init__()
        self.setFixedSize(800, 600)  

        self.stack = QStackedWidget()

        self.start_view = StartView()
        self.quiz_view = QuizView()
        self.result_view = ResultView()
        self.stack = QStackedWidget()


        self.stack.addWidget(self.start_view)
        self.stack.addWidget(self.quiz_view)
        self.stack.addWidget(self.result_view)

        # Créer un layout vertical pour contenir le QStackedWidget
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        
app = QApplication(sys.argv) # Crée l'application
#app.setStyle("Fusion")

with open("Resources/style.qss") as f:
    app.setStyleSheet(f.read())

window= MainWindow()
m=QuizModel()
c=QuizController(m, window)
window.show() # Affiche la fenêtre

app.setWindowIcon(QIcon("resources/quizicon.png"))
sys.exit(app.exec_()) # Lance la boucle de l'application et quitte proprement
