#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 01:43:51 2026

@author: samahbouzidi
"""

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
class ResultView(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.result_label = QLabel("Score : 0")
        self.restart_button = QPushButton("Recommencer")
        layout.addWidget(self.result_label)
        layout.addWidget(self.restart_button)
        self.setLayout(layout)