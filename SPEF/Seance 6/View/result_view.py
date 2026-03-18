#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:43:51 2026

@author: samahbouzidi
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class ResultView(QWidget):

    def __init__(self):

        super().__init__()
        self.setObjectName("resultScreen")
        #------- Background Image ---------
        self.bg_label = QLabel(self)
        pixmap = QPixmap("Resources/result.png")
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()

        layout = QVBoxLayout()
        self.result_label = QLabel("Score : 0")
        self.restart_button = QPushButton("Recommencer")

        layout.addWidget(self.result_label)
        layout.addWidget(self.restart_button)
        
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        
    def resizeEvent(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)