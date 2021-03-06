import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0,0,0))
        p.setBrush(QColor(0,127,0))
        p.drawPolygon([QPoint(70,100), QPoint(100,110), QPoint(130,100), QPoint(100,150)])
        p.setPen(QColor(255,127,0))
        p.setBrush(QColor(255,127,0))
        p.drawPie(50,150,100,100,0,180 * 16)
        p.drawPolygon([QPoint(50,200), QPoint(150,200), QPoint(100,400)])
        p.drawPixmap(QRect(200,100,320,320), self.rabbit)
        p.end()

class Simple_drawing_John(Simple_drawing_window):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("john Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)


        p.setPen(QColor(255, 255, 0))
        p.setBrush(QColor(255, 255, 0))
        p.drawPie(20, 50, 200, 200, 0, 180 * 360)

        p.setPen(QColor(240, 240, 240))
        p.setBrush(QColor(240, 240, 240))
        p.drawPie(0, 50, 150, 150, 0, 180 * 360)

        p.setPen(QColor(255, 255, 255))
        p.setBrush(QColor(255, 255, 255))
        p.drawPie(0, 250, 80, 80, 0, 180 * 360)
        p.drawPie(50, 250, 80, 80, 0, 180 * 360)
        p.drawPie(100, 250, 80, 80, 0, 180 * 360)
        p.drawPie(150, 250, 80, 80, 0, 180 * 360)
        p.drawPie(200, 250, 80, 80, 0, 180 * 360)
        p.drawPie(150, 250, 80, 80, 0, 180 * 360)
        p.drawPie(100, 200, 80, 80, 0, 180 * 360)
        p.drawPie(150, 200, 80, 80, 0, 180 * 360)

        p.drawPie(0, 250, 80, 80, 0, 180 * 360)
        p.drawPie(350, 250, 80, 80, 0, 180 * 360)
        p.drawPie(400, 250, 80, 80, 0, 180 * 360)
        p.drawPie(450, 250, 80, 80, 0, 180 * 360)
        p.drawPie(500, 250, 80, 80, 0, 180 * 360)
        p.drawPie(450, 250, 80, 80, 0, 180 * 360)
        p.drawPie(400, 200, 80, 80, 0, 180 * 360)
        p.drawPie(450, 200, 80, 80, 0, 180 * 360)


        p.drawPixmap(QRect(400, 380, 100, 100), self.rabbit)


def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_John()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())