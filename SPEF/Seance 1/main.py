import sys
from PyQt5.QtWidgets import QApplication
from view.quiz_view import QuizView

app = QApplication(sys.argv) # Crée l'application
window = QuizView() # Crée la fenêtre
window.show() # Affiche la fenêtre
sys.exit(app.exec_()) # Lance la boucle de l'application et quitte proprement
