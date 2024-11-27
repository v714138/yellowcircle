import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from main_ui import Ui_MainWindow


class Suprematism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.draw)
    def draw(self):
        self.update()

    def paintEvent(self, event):
        w = randint(0, 200)
        qp = QPainter()
        qp.begin(self)
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        qp.drawEllipse(200, 200, w, w)
        qp.drawEllipse(400, 400, w, w)
        qp.end()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())