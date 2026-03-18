#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:43:37 2026

@author: samahbouzidi
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
class StartView(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("startScreen")

        # Background image
        self.bg_label = QLabel(self)
        pixmap = QPixmap("Resources/start.png")
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()

        # Overlay
        self.overlay = QLabel(self)
        self.overlay.setStyleSheet("background-color: rgba(0,0,0,100);")
        self.overlay.lower()

        # Widgets
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.title = QLabel("Bienvenue dans le Quiz")
        self.start_button = QPushButton("Commencer")
        layout.addWidget(self.title)
        layout.addWidget(self.start_button)
        self.setLayout(layout)


    def resizeEvent(self, event):
        # adapter bg_label et overlay à la taille de la fenêtre
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.overlay.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)


