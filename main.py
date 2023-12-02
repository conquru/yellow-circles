import sys
from random import randint
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic 


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.creat.clicked.connect(self.creat_circle)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_flag(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()
    
    def creat_circle(self, qp):
        qp.setBrush(QColor('Yellow'))
        x, y = [randint(10, 500) for i in range(2)]
        w, h = [randint(10, 100) for i in range(2)]        
        qp.drawEllipse(x, y, w, h)

    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
