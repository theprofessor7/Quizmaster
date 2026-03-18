# Controller/quiz_controller.py

from PyQt5.QtWidgets import QMessageBox


class QuizController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        # Connexions boutons
        self.view.next_button.clicked.connect(self.next_question)
        self.view.prev_button.clicked.connect(self.prev_question)

        # Initialisation interface
        self.view.progress_bar.setMaximum(len(self.model.questions))
        self.view.prev_button.setEnabled(False)

    def start(self):
        self.update_view()

    def update_view(self):
        current = self.model.get_current_question()

        # Mettre à jour question + réponses
        self.view.update_question(current["question"], current["answers"])

        # Progression
        self.view.progress_bar.setValue(self.model.current_index + 1)

        # Score
        self.view.update_score(self.model.score)

        # Bouton précédent
        self.view.prev_button.setEnabled(self.model.current_index > 0)

        # Texte bouton suivant
        if self.model.current_index < len(self.model.questions) - 1:
            self.view.next_button.setText("Suivant")
        else:
            self.view.next_button.setText("Terminer")

    def next_question(self):
        selected = self.view.get_selected_answer()
        if selected is None:
            QMessageBox.information(
                self.view,
                "Réponse",
                "Choisis une réponse avant de continuer."
            )
            return

        # Empêcher de compter plusieurs fois la même question
        if self.model.current_index not in self.model.answered_questions:
            self.model.answered_questions.add(self.model.current_index)
            self.model.check_answer(selected)

        # Question suivante ou fin
        if self.model.current_index + 1 < len(self.model.questions):
            self.model.current_index += 1
            self.update_view()
        else:
            QMessageBox.information(
                self.view,
                "Quiz terminé",
                f"Score final : {self.model.score} / {len(self.model.questions)}"
            )
            self.view.update_score(self.model.score)
            self.view.next_button.setEnabled(False)
            self.view.prev_button.setEnabled(True)

    def prev_question(self):
        if self.model.current_index > 0:
            self.model.current_index -= 1
            self.update_view()

            # Griser les réponses si la question a déjà été validée
            if self.model.current_index in self.model.answered_questions:
                for rb in self.view.radio_buttons:
                    rb.setEnabled(False)
            else:
                for rb in self.view.radio_buttons:
                    rb.setEnabled(True)