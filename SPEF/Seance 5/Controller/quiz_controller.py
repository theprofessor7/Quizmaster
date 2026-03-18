#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 16:02:54 2026

@author: samahbouzidi
"""
START_PAGE=0
QUIZ_PAGE=1
RESULT_PAGE=2

from PyQt5.QtWidgets import QMessageBox
    
class QuizController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.quiz_view.progress_bar.setMaximum(len(self.model.questions))
        self.update_view()
        self.view.quiz_view.prev_button.setEnabled(False)
        self.view.quiz_view.next_button.clicked.connect(self.next_question)
        self.view.quiz_view.prev_button.clicked.connect(self.prev_question)
        self.view.start_view.start_button.clicked.connect(self.start_quiz)
        self.view.result_view.restart_button.clicked.connect(self.restart)
        
    def update_view(self):
        current = self.model.get_current_question()
        self.view.quiz_view.update_question(current["question"], current["answers"])
        self.view.quiz_view.progress_bar.setValue(self.model.current_index+1)
        self.view.quiz_view.update_score(f"{self.model.score}")
    
    def next_question(self):
        selected_button = self.view.quiz_view.button_group.checkedButton()
        if not selected_button :
            QMessageBox.warning(self.view, "Erreur", "Attention Vous devez séléectionner une réponse")
            return 
        answer = selected_button.text()
        if self.model.current_index not in self.model.answered_questions:
            
            is_correct = self.model.check_answer(answer)
            self.model.answered_questions.add(self.model.current_index)
            if self.model.current_index+1 < len(self.model.questions):
                self.model.current_index += 1
                self.update_view()
            else:
                self.show_result()
                self.view.quiz_view.prev_button.setEnabled(True)
            
    def prev_question(self):
        if self.model.current_index >0:
            self.model.current_index-=1
            self.update_view()
            for b in self.view.radio_buttons:
                b.setEnabled(False)
                
    def start_quiz(self):
        self.view.stack.setCurrentIndex(QUIZ_PAGE)
        
    def restart(self):
        self.model.current_index=0
        self.model.score=0
        self.model.answered_questions=set()
        self.update_view()
        self.view.stack.setCurrentIndex(START_PAGE)
    def show_result(self):
        # Récupérer le score final depuis le modèle
        score = self.model.score
    
        # Mettre à jour le label de la vue résultat avec le score
        self.view.result_view.result_label.setText(f"Score final : {score}")
    
        # Passer à la page des résultats dans la pile de vues
        self.view.stack.setCurrentIndex(RESULT_PAGE)


        