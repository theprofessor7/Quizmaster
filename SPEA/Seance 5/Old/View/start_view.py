# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 16:25:59 2026

@author: $IM7000-R38UPG6NC3F0
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

class StartView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.title = QLabel("Bienvenue dans le Quiz")
        self.start_button = QPushButton("Commencer")
        layout.addWidget(self.title)
        layout.addWidget(self.start_button)
        self.setLayout(layout)