#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:43:37 2026

@author: samahbouzidi
"""
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class StartView(QWidget):

    def __init__(self):

        super().__init__()
        
        self.setObjectName("startScreen")
        
        #------- Background Image ---------
        self.bg_label = QLabel(self)
        pixmap = QPixmap("Resources/start.png")
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.lower()
                
        layout = QVBoxLayout()
        self.title = QLabel("Bienvenue dans le Quiz")
        self.start_button = QPushButton("Commencer")

        layout.addWidget(self.title)
        layout.addWidget(self.start_button)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
        
    def resizeEvent(self, event):
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        super().resizeEvent(event)

