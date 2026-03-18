import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QStackedWidget, QVBoxLayout

from View.quiz_view import QuizView
from Model.quiz_model import QuizModel
from Controller.quiz_controller import QuizController

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget()
        self.start_view = StartView()
        self.quiz_view = QuizView()
        self.result_view = ResultView()
        
        self.stack.setStyleSheet("background-color: lightblue;")
        self.start_view.setStyleSheet("background-color: lightblue")
        self.result_view.setStyleSheet("background-color: lightblue")
        
        # Suite
        self.stack.addWidget(self.start_view)
        self.stack.addWidget(self.quiz_view)
        self.stack.addWidget(self.result_view)
        
        # Créer un layout vertical pour contenir le QStackedWidget
        layout = QVBoxLayout()
        layout.addWidget(self.stack)
        self.setLayout(layout)
        
"""app = QApplication(sys.argv)
app.setWindowIcon(QIcon("Resources/quizicon.png"))
#app.setStyle("Fusion")   # utile pour la progress bar, surtout sur Mac

model = QuizModel()
view = QuizView()
controller = QuizController(model, view)

view.show()
controller.start()

sys.exit(app.exec_())"""

window= MainWindow()
