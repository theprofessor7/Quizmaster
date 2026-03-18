#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 16:02:10 2026

@author: samahbouzidi
"""

from PyQt5.QtWidgets import QProgressBar,QPushButton,QHBoxLayout,QRadioButton,QWidget,QLabel,QVBoxLayout,QButtonGroup
from PyQt5.QtCore import Qt
class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.setStyleSheet("background-color: lightblue;")
        self.setMinimumSize(400, 300)
        self.question_label = QLabel("Quelle est la capitale de la France ?", self)
        self.question_label.setAlignment(Qt.AlignCenter)
        
        header_layout = QHBoxLayout()
        self.score_label1 = QLabel("Score:")
        self.score_label2 = QLabel("0")
        header_layout.addWidget(self.question_label)
        header_layout.addStretch()  # pousse le score à droite
        header_layout.addWidget(self.score_label1)
        header_layout.addWidget(self.score_label2)
        #-----answer layout---
        #créer le layout
        self.answer_layout=QVBoxLayout()
        #créer le button groupe
        self.button_group=QButtonGroup()
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("%p%")  # %p% affiche le pourcentage
        self.answer_layout.addWidget(self.progress_bar)
        #créer les boutons radio
        self.radio_buttons = []
        for _ in range(4):  # 4 réponses possibles
            rb = QRadioButton("")
            self.button_group.addButton(rb)
            self.radio_buttons.append(rb)
            self.answer_layout.addWidget(rb)
            
        # layout navigation
        self.navigation_layout=QHBoxLayout()
        self.prev_button=QPushButton("Précédent")
        self.next_button=QPushButton("Suivant")
        self.navigation_layout.addWidget(self.prev_button)
        self.navigation_layout.addWidget(self.next_button)
        #---main layout---
        main_layout = QVBoxLayout()
        main_layout.addLayout(header_layout)
        main_layout.addLayout(self.answer_layout)
        main_layout.addLayout(self.navigation_layout)
        self.setLayout(main_layout) # Application du layout à la fenêtre
        # ----- Style -----
        self.setStyleSheet("background-color: lightblue;")
        
    def update_question(self, question, answers):
        self.question_label.setText(question)
        for rb, text in zip(self.radio_buttons, answers):
            rb.setChecked(False)
            rb.setText(text)
    def update_score(self, score):
        self.score_label2.setText(score)