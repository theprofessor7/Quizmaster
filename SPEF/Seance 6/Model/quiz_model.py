#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  6 16:03:12 2026

@author: samahbouzidi
"""
import json
class QuizModel:
    def __init__(self, json_file="Resources/questions.json"):
        self.questions=self.load_questions(json_file)
        self.current_index=0
        self.score=0
        self.answered_questions = set()
    def get_current_question(self):
        return self.questions[self.current_index]
    def check_answer(self, answer):
        if answer == self.get_current_question()["correct"]:
            self.score += 1
            return True
        return False
        
    def load_questions(self, json_file):
        """Charge les questions depuis un fichier JSON"""
        with open(json_file, "r", encoding="utf-8") as file:
            return json.load(file)
        
        
        