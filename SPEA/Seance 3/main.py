import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

#-- importer la vue, le contrôleur et le modèle
from View.quiz_view import QuizView
from Controller.quiz_controller import QuizController
from Model.quiz_model import QuizModel

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("resources/quizicon.png"))

#-- instancier la vue, le modèle et le contrôleur
model = QuizModel()
view = QuizView()
controller = QuizController(model,view)
view.show()
sys.exit(app.exec_()) 