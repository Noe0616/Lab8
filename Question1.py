import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawing_window4(QWidget):
    def __init__(self):
        QWidget.__init__(self , None)
        self.setWindowTitle("SImple Drawing")

    def paintEvent(self , e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0 , 0 , 0))
        p.setBrush(QColor(0 , 0 , 0))
        p.drawPie(500 , 50 , 100 ,100 , 0 , 180 * 32)
        p.drawPie(400, 50, 100, 100, 0, 180 * 32)
        p.drawPie(450, 120, 100, 100, 0, 180 * 32)
        p.end()

def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window4()
    w.show()

    return app.exec_()

if __name__ == '__main__':
    sys.exit(main())