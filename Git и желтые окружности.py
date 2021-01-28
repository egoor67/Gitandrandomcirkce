import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QWidget
from PyQt5 import QtGui
from PyQt5.QtCore import QRect,Qt
from PyQt5.QtGui import QPainter,QBrush, QPen
from PyQt5 import QtCore
from PyQt5.QtGui import QPainter, QColor, QFont

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, git_and_yellow_circle):
        git_and_yellow_circle.setObjectName("git_and_yellow_circle")
        git_and_yellow_circle.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(git_and_yellow_circle)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 0, 111, 41))
        self.pushButton.setObjectName("pushButton")
        git_and_yellow_circle.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(git_and_yellow_circle)
        self.statusbar.setObjectName("statusbar")
        git_and_yellow_circle.setStatusBar(self.statusbar)

        self.retranslateUi(git_and_yellow_circle)
        QtCore.QMetaObject.connectSlotsByName(git_and_yellow_circle)

    def retranslateUi(self, git_and_yellow_circle):
        _translate = QtCore.QCoreApplication.translate
        git_and_yellow_circle.setWindowTitle(_translate("Ui_MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("git_and_yellow_circle", "ТЫКНИ"))

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # uic.loadUi('UI.ui', self)
        self.setupUi(self)
        self.n = [Qt.white, Qt.black, Qt.red, Qt.darkRed, Qt.green, Qt.darkGreen, Qt.darkGray, Qt.lightGray]
        self.setWindowTitle('Git и случайные окружности')
        self.should_paint_circle = False
        self.pushButton.clicked.connect(self.run)

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.should_paint_circle:
            s = random.randint(5, 100)
            painter = QtGui.QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            f = random.randint(0, 7)
            painter.setPen(QPen(self.n[f], s, Qt.SolidLine))
            painter.drawEllipse(640 // 2, 480 // 2, s, s)

    def run(self):
        self.should_paint_circle = True
        self.update()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
