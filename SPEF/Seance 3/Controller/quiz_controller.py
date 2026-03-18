from PyQt5.QtWidgets import QMessageBox

class QuizController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        # Ajuster le nom du bouton en fonction du nom utilisé dans la vue
        self.view.next_button.clicked.connect(self.next_question)
        
    def next_question(self):
        selected_button = self.view.button_group.checkedButton()
        if not selected_button:
            QMessageBox.warning(self.view, "Attention","Veuillez sélectionner une réponse.")
            return
            
        answer = selected_button.text()
        
        is_correct = self.model.check_answer(answer)
        if is_correct:
            QMessageBox.information(self.view, "Résultat", "Bonne réponse ")
        else:
            QMessageBox.information(self.view, "Résultat", "Mauvaise réponse ")
        print("Score actuel :", self.model.score)
