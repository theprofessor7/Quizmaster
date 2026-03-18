from PyQt5.QtWidgets import QWidget, QLabel, QRadioButton, QPushButton, QVBoxLayout, QHBoxLayout, QButtonGroup
from PyQt5.QtCore import Qt

class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.resize(400, 300)
        self.question_label = QLabel("Quelle est la capitale de la France ?", self)
        self.question_label.setAlignment(Qt.AlignCenter)
        
        # ----- Answer Layout -----
        self.button_group = QButtonGroup(self)
        
        self.radio_paris = QRadioButton("Paris", self)
        self.radio_lyon = QRadioButton("Lyon", self)
        self.radio_marseille = QRadioButton("Marseille", self)
        self.radio_bordeaux = QRadioButton("Bordeaux", self)
        
        self.button_group.addButton(self.radio_paris)
        self.button_group.addButton(self.radio_lyon)
        self.button_group.addButton(self.radio_marseille)
        self.button_group.addButton(self.radio_bordeaux)

        answer_layout = QVBoxLayout()
        answer_layout.addWidget(self.question_label)
        answer_layout.addWidget(self.radio_paris)
        answer_layout.addWidget(self.radio_lyon)
        answer_layout.addWidget(self.radio_marseille)
        answer_layout.addWidget(self.radio_bordeaux)
        
        # ----- Boutons navigation -----
        self.prev_button = QPushButton("Précédent")
        self.next_button = QPushButton("Suivant")
        
        # ----- Layout navigation_ -----
        navigation_layout = QHBoxLayout()
        navigation_layout.addWidget(self.prev_button)
        navigation_layout.addWidget(self.next_button)
        
        # ----- Layout principal -----
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.question_label)
        main_layout.addLayout(answer_layout)
        main_layout.addLayout(navigation_layout)
        self.setLayout(main_layout) # Application du layout à la fenêtre
        
        # ----- Style -----
        self.setStyleSheet("background-color: lightblue;")
 


