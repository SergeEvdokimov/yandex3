import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from random import randrange


class Painter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 200, 800, 600)
        self.need_new = False
        self.pushButton = QPushButton('Нарисовать', self)
        self.pushButton.move(350, 30)
        self.pushButton.clicked.connect(self.draw)
        self.color = QColor(0, 0, 0)

    def draw(self):
        self.need_new = True
        self.update()

    def paintEvent(self, event):
        if self.need_new:
            qp = QPainter()
            qp.begin(self)
            count = randrange(1, 10)
            for _ in range(count):
                self.color = QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255))
                qp.setBrush(QBrush(self.color, Qt.SolidPattern))
                x, y, r = randrange(50, 700), randrange(50, 500), randrange(10, 100)
                qp.drawEllipse(x, y, r, r)
            qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Painter()
    ex.show()
    sys.exit(app.exec_())
