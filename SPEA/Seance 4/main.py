import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from View.quiz_view import QuizView
from Model.quiz_model import QuizModel
from Controller.quiz_controller import QuizController


app = QApplication(sys.argv)
app.setWindowIcon(QIcon("Resources/quizicon.png"))
#app.setStyle("Fusion")   # utile pour la progress bar, surtout sur Mac

model = QuizModel()
view = QuizView()
controller = QuizController(model, view)

view.show()
controller.start()

sys.exit(app.exec_())