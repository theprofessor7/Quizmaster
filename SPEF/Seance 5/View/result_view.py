#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:43:51 2026

@author: samahbouzidi
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class ResultView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.setObjectName("resultScreen")
        
        # Background image
        self.bg_label = QLabel(self)
        pixmap = QPixmap("Resources/result.png")
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()

        # Overlay
        self.overlay = QLabel(self)
        self.overlay.setStyleSheet("background-color: rgba(0,0,0,100);")
        self.overlay.lower()

        self.result_label = QLabel("Score : 0")
        self.restart_button = QPushButton("Recommencer")
        self.result_label.setObjectName("resultLabel")
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.result_label)
        layout.addWidget(self.restart_button)
        self.setLayout(layout)
        
        
    def resizeEvent(self, event):
        # adapter bg_label et overlay à la taille de la fenêtre
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.overlay.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)