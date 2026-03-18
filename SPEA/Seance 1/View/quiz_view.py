from PyQt5.QtWidgets import QWidget

class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QuizMaster")
        self.resize(400, 300)