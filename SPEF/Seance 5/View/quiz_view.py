#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (
    QProgressBar, QPushButton, QHBoxLayout, QRadioButton,
    QWidget, QLabel, QVBoxLayout, QButtonGroup
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class QuizView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QuizMaster")
        #self.setObjectName("quizScreen")

        # ---------------- Background image ----------------
        self.bg_label = QLabel(self)
        self.bg_label.setPixmap(QPixmap("Resources/quizview.jpg"))
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()


        # ---------------- Question ----------------
        self.question_label = QLabel("Quelle est la capitale de la France ?")
        self.question_label.setAlignment(Qt.AlignCenter)

        # ---------------- Header ----------------
        header_layout = QHBoxLayout()

        self.score_label1 = QLabel("Score :")
        self.score_label2 = QLabel("0")

        header_layout.addWidget(self.question_label)
        header_layout.addStretch()
        header_layout.addWidget(self.score_label1)
        header_layout.addWidget(self.score_label2)

        # ---------------- Réponses ----------------
        self.answer_layout = QVBoxLayout()
        self.button_group = QButtonGroup()
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("%p%")

        self.answer_layout.addWidget(self.progress_bar)

        self.radio_buttons = []

        for _ in range(4):
            rb = QRadioButton("")
            self.button_group.addButton(rb)
            self.radio_buttons.append(rb)
            self.answer_layout.addWidget(rb)

        # ---------------- Navigation ----------------
        navigation_layout = QHBoxLayout()
        self.prev_button = QPushButton("Précédent")
        self.next_button = QPushButton("Suivant")
        navigation_layout.addWidget(self.prev_button)
        navigation_layout.addWidget(self.next_button)

        # ---------------- Layout principal ----------------
        main_layout = QVBoxLayout()
        main_layout.addLayout(header_layout)
        main_layout.addLayout(self.answer_layout)
        main_layout.addLayout(navigation_layout)
        main_layout.setAlignment(Qt.AlignCenter)

        self.setLayout(main_layout)

        # ---------------- ObjectName pour QSS ----------------
        self.question_label.setObjectName("questionLabel")
        self.score_label2.setObjectName("scoreLabel")

    # ---------------- Update question ----------------
    def update_question(self, question, answers):
        self.question_label.setText(question)

        for rb, text in zip(self.radio_buttons, answers):
            rb.setChecked(False)
            rb.setText(text)

    # ---------------- Update score ----------------
    def update_score(self, score):
        self.score_label2.setText(score)

    # ---------------- Resize background ----------------
    def resizeEvent(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)