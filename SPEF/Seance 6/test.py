import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

# ---------------- StartView ----------------
class StartView(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Start View")
        self.resize(800, 600)
        self.setObjectName("startScreen")

        # Background image
        self.bg_label = QLabel(self)
        pixmap = QPixmap("Resources/start.png")
        self.bg_label.setPixmap(pixmap)
        self.bg_label.setScaledContents(True)
        self.bg_label.setGeometry(0, 0, self.width(), self.height())
        self.bg_label.lower()

        # Overlay
        self.overlay = QLabel(self)
        self.overlay.setStyleSheet("background-color: rgba(0,0,0,100);")
        self.overlay.setGeometry(0, 0, self.width(), self.height())
        self.overlay.lower()

        # Widgets
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.title = QLabel("Bienvenue dans le Quiz")
        self.start_button = QPushButton("Commencer")
        layout.addWidget(self.title)
        layout.addWidget(self.start_button)
        self.setLayout(layout)




# ---------------- Main ----------------
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Charger le QSS
    with open("Resources/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    start_view = StartView()
    start_view.show()


    sys.exit(app.exec_())