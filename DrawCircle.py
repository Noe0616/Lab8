import sys
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *

class Simple_drawwing_windoww(QWidget):
    def __init__(self):
        QWidget.__init__(self,None)
        self.setWindowTitle("Simple drawing")
        self.dragon=QPixmap("images/rabbit.png")

    def paintEvent(self,e):
        p=QPainter()
        p.begin(self)

        p.setPen(QColor(230,230,0))
        p.setBrush(QColor(230,230,0))
        p.drawPie(25,25,150,150,0,360*16)
        p.drawPixmap(QRect(200,100,320,320), self.dragon)
        p.end()

def main():
    app=QApplication(sys.argv)
    w= Simple_drawwing_windoww()
    w.show()

    return app.exec_()

if __name__ == "__main__":
    sys.exit(main())