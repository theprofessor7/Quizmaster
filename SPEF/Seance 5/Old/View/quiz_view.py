from PyQt5.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QRadioButton, QPushButton,
    QHBoxLayout, QProgressBar, QButtonGroup
)
from PyQt5.QtCore import Qt


class QuizView(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QuizMaster")
        self.resize(500, 350)

        # ---------- Question ----------
        self.question_label = QLabel("Question")
        self.question_label.setAlignment(Qt.AlignCenter)

        # ---------- Score ----------
        self.score_label1 = QLabel("Score :")
        self.score_label2 = QLabel("0")

        self.header_layout = QHBoxLayout()
        self.header_layout.addWidget(self.question_label)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.score_label1)
        self.header_layout.addWidget(self.score_label2)

        # ---------- Réponses ----------
        self.answers_layout = QVBoxLayout()
        self.answers_layout.setSpacing(15)
        self.answers_layout.setContentsMargins(20, 20, 20, 20)

        # Barre de progression
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.progress_bar.setFormat("%p%")
        self.answers_layout.addWidget(self.progress_bar)

        # Groupe de boutons radio
        self.button_group = QButtonGroup(self)
        self.radio_buttons = []

        for _ in range(4):
            rb = QRadioButton("")
            self.button_group.addButton(rb)
            self.radio_buttons.append(rb)
            self.answers_layout.addWidget(rb)

        # ---------- Navigation ----------
        self.navigation_layout = QHBoxLayout()
        self.navigation_layout.setSpacing(30)

        self.prev_button = QPushButton("Précédent")
        self.next_button = QPushButton("Suivant")

        self.navigation_layout.addWidget(self.prev_button)
        self.navigation_layout.addWidget(self.next_button)

        # ---------- Layout principal ----------
        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.header_layout)
        self.main_layout.addLayout(self.answers_layout)
        self.main_layout.addLayout(self.navigation_layout)
        self.setLayout(self.main_layout)

        # ---------- Style ----------
        self.setStyleSheet("background-color: lightblue;")
        self.question_label.setStyleSheet("font-size: 16px; font-weight: bold;")

    def update_question(self, question, answers):
        """Met à jour la question et les réponses."""
        self.question_label.setText(question)
        for rb, text in zip(self.radio_buttons, answers):
            rb.setChecked(False)
            rb.setText(text)
            rb.setEnabled(True)

    def update_score(self, score):
        """Met à jour l'affichage du score."""
        self.score_label2.setText(str(score))

    def get_selected_answer(self):
        """Retourne le texte de la réponse cochée, ou None."""
        for rb in self.radio_buttons:
            if rb.isChecked():
                return rb.text()
        return None

    def clear_selection(self):
        """Décoche toutes les réponses."""
        for rb in self.radio_buttons:
            rb.setAutoExclusive(False)
            rb.setChecked(False)
            rb.setAutoExclusive(True)
            