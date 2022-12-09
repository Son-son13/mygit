import sys

from random import randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel
from PyQt5.QtGui import QPainter


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Суперматизм')
        self.setMouseTracking(True)
        self.type = 3
        self.flag = False
        self.coords = [150, 150]
        self.qp = QPainter()

    def chache_flag(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def mousePressEvent(self, event):
        self.coords = [event.x(), event.y()]
        if event.button() == Qt.LeftButton:
            self.type = 1
        elif event.button() == Qt.RightButton:
            self.type = 2
        self.chache_flag()


    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.type = 3
        self.draw()


    def draw(self):
        a = randint(20, 100)
        if self.type == 1:
            self.qp.drawEllipse(*self.coords, a, a)
        elif self.type == 2:
            self.qp.drawRect(*self.coords, a, a)
        elif self.type == 3:
            x, y = self.coords
            R = int(a * 3 ** (1/2) / 3)
            h = int(a * 3 ** (1/2) / 2)
            coords = [(x, y - R), (x + a // 2, y + h), (x - a // 2, y + h)]
            self.qp.drawLine(*coords[0], *coords[1])
            self.qp.drawLine(*coords[1], *coords[2])
            self.qp.drawLine(*coords[2], *coords[0])

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())