# -*- coding: utf-8 -*-
import sys
from random import choice
from PyQt5.QtWidgets import  QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QLCDNumber, QMessageBox
from PyQt5 import QtGui 


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def unitUI(self):
        self.setGeometry(400, 400, 900, 600)
        self.MinimumSize(900, 600)
        self.MaximumSize(900, 600)
        self.setWindowTitle('Развивающая игра')
        
        self.title = QLabel(self)
        self.title.setText('Математический тренажер')
        self.title.setFont(QtGui.QFont("Times", 20, QtGui.QFont.Bold))
        self.title.move(350, 40)
        
        self.btn = QPushButton('Начать', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(250, 60)
        #self.btn.clicked.connect(self.start)
        
        self.rules = QPushButton('Правила', self)
        self.rules.resize(self.btn.sizeHint())
        self.rules.move(500, 70)
        self.rules.clicked.connect(self.info)
        
        self.end = QPushButton('Итог', self)
        self.end.resize(self.btn.sizeHint())
        self.end.move(450, 560)
        self.end.clicked.connect(self.finish)
        
        self.label1 = QLabel(self)
        self.label1.setText('Правильно:')
        self.label1.move(650, 250)
        self.ok1 = QLCDNumber(self)
        self.ok1.move(800, 290)
        
        self.label2 = QLabel(self)
        self.label2.setText('Ошибки:')
        self.label2.move(750, 350)
        self.ok2 = QLCDNumber(self)
        self.ok2.move(780, 360)
        
        self.x1 = QLabel(self)
        self.x1.move(50, 170)
        
        self.x2 = QLabel(self)
        self.x2.move(50, 210)
        
        self.x3 = QLabel(self)
        self.x3.move(50, 260)

        self.x4 = QLabel(self)
        self.x4.move(50, 310)
        
        self.y1 = QLineEdit(self)
        self.y1.resize(40, 30)
        self.y1.move(180, 170)
        self.xy1 = QPushButton('ОК', self)
        self.xy1.resize(40, 30)
        self.xy1.move(250, 150)
        self.xy1.clicked.connect(self.go1)   
        
        self.y2 = QLineEdit(self)
        self.y2.resize(40, 30)
        self.y2.move(180, 200)
        self.xy2 = QPushButton('ОК', self)
        self.xy2.resize(250, 200)
        self.xy2.clicked.connect(self.go2)
        
        self.y3 = QLineEdit(self)
        self.y3.resize(40,30)
        self.y3.move(180, 230)
        self.xy3 = QPushButton('ОК', self)
        self.xy3.resize(40, 30)
        self.xy3.move(250, 250)
        self.xy3.clicked.coonect(self.go3)
        
        self.y4 = QLineEdit(self)
        self.y4.resize(40, 30)
        self.y4.move(180, 250)
        self.xy4 = QPushButton('ОК', self)
        self.xy4.resize(40, 30)
        self.xy4.move(250, 290)
        self.xy4.cliced.connect(self.go4)
        
        self.z1 = QLabel(self)
        self.z1.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z1.resize(40, 40)
        self.z1.move(500, 300)
        
        self.z2 = QLabel(self)
        self.z2.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z2.resize(40, 40)
        self.z2.move(560, 320)
        
        self.z3 = QLabel(self)
        self.z3.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z3.resize(40, 40)
        self.z3.move(500, 400)
        
        self.z4 = QLabel(self)
        self.z4.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z4.resize(40,40)
        self.move(540, 400)
        
        self.z5 = QLabel(self)
        self.z5.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z5.resize(40, 40)
        self.z5.move(440, 420)
        
        self.z6 = QLabel(self)
        self.z6.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z6.resize(40, 40)
        self.z6.move(580, 390)
        
        self.z7 = QLabel(self)
        self.z7.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z7.resize(40, 40)
        self.z7.resize(390, 190)
        
        self.z8 = QLabel(self)
        self.z8.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z8.resize(40, 40)
        self.z8.move(470, 350)
        
        self.z9 = QLabel(self)
        self.z9.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z9.resize(40, 40)
        self.z9.move(390, 390)
        
        self.z10 = QLabel(self)
        self.z10.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z10.resize(40, 40)
        self.z10.move(400, 390)

        self.z11 = QLabel(self)
        self.z11.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z11.resize(40, 40)
        self.z11.move(430, 390)
         
        self.z12 = QLabel(self)
        self.z12.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z12.resize(40, 40)
        self.z12.move(450, 300)
        
        self.z13 = QLabel(self)
        self.z13.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z13.resize(40, 40)
        self.z13.move(350, 3470)
        
        self.z14 = QLabel(self)
        self.z14.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z14.resize(40, 40)
        self.move(540, 160)
        
        self.z15 = QLabel(self)
        self.z15.setFont(QtGui.QFont("Times", 12, QtGui.QFont.Bold))
        self.z15.resize(40, 40)
        self.z15.move(460, 180)
        
        self.n1 = 0
        self.n2 = 0
        self.n3 = 0
        self.n4 = 0
        self.n5 = 0
        self.n6 = 0
        self.n7 = 0
        self.count1 = 0
        self.count2 = 0
        self.count3 = 0
        
    def info(self):
        i1 = "Вам нужно решить 10 математических примеров. Когда вы решите все примеры Вы узнаете количество набранных баллов."
        i2 = "Вам предоставлены будут возможность решить новые примеры, либо выйти из игры."
        msg = QMessageBox()
        msg.move(550, 500)
        msg.setWindowTitle("Правила игры")
        msg.setText(i1 + "\n" + i2)
        msg.exec()

    def finish(self):
        msg = QMessageBox()
        msg.move(600, 500)
        msg.setWindowTitle("Итог")
        msg.setText("Количество правильных ответов: {}".format(self.correct))
        msg.exec()
        
    def start(self):
        array1 = list(range(2, 10))
        array2 = list(range(2, 10))
        array3 = list(range(2, 10))
        array4 = list(range(2, 10))
        array5 = list(range(0, 20))
        array6 = list(range(0, 20))
        array7 = list(range(0, 20))

        self.n1 = choice(array1)
        self.n2 = choice(array2)
        self.n3 = choice(array3)
        self.n4 = choice(array4)
        self.n5 = choice(array5)
        self.n6 = choice(array6)
        self.n7 = choice(array7)

        self.count1 = 0
        self.count2 = 0 
        self.correct = 0
        self.ok1.display(self.count1)
        self.ok2.display(self.count2)

        self.xy1.setEnabled(True)
        self.xy2.setEnabled(True)
        self.xy3.setEnabled(True)
        self.xy4.setEnabled(True)
       
        self.y1.setText("")
        self.y2.setText("")
        self.y3.setText("")
        self.y4.setText("")
       
        pal = self.z1.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z1.setPalette(pal)
       
        pal = self.z2.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z2.setPalette(pal)
       
        pal = self.z3.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z3.setPalette(pal)
 
        pal = self.z4.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z4.setPalette(pal)
       
        pal = self.z5.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z5.setPalette(pal)
       
        pal = self.z6.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z6.setPalette(pal)
       
        pal = self.z7.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z7.setPalette(pal)
       
        pal = self.z8.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z8.setPalette(pal)

        pal = self.z9.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z9.setPalette(pal)               

        pal = self.z10.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z10.setPalette(pal)
       
        pal = self.z11.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z11.setPalette(pal)
          
        pal = self.z12.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z12.setPalette(pal)        
        
        pal = self.z13.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z13.setPalette(pal)
       
        pal = self.z14.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z14.setPalette(pal)
       
        pal = self.z15.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("black"))
        self.z15.setPalette(pal)
       
        self.x1.setText("в,,-1:    {} : {} = ".format(self.n1, self.n2))
        self.x1.resize(self.x1.sizeHint())
       
        self.x2.setText("в,,-2:    {} : {} = ".format(self.n3, self.n4))
        self.x2.resize(self.x2.sizeHint())
       
        self.x3.setText("в,,-3:    {} : {} = ".format(self.n5, self.n2))
        self.x3.resize(self.x3.sizeHint())
       
        self.x4.setText("в,,-4:    {} : {} = ".format(self.n3, self.n1))
        self.x4.resize(self.x4.sizeHint())
       
        self.z1.setText("{}".format(self.n2 / self.n1))
        self.z2.setText("{}".format(self.n3 / self.n4))
        self.z3.setText("{}".format(self.n5 / self.n2))
        self.z4.setText("{}".format(self.n1 / self.n3))
        self.z5.setText("{}".format(self.n6 / self.n7))
        self.z6.setText("{}".format(self.n4 / self.n6))
        self.z7.setText("{}".format(self.n3 / self.n2))
        self.z8.setText("{}".format(self.n5 / self.n3))
        self.z9.setText("{}".format(self.n6 / self.n2))
        self.z10.setText("{}".format(self.n3 / self.n4))
        self.z11.setText("{}".format(self.n5 / self.n2))
        self.z12.setText("{}".format(self.n1 / self.n5))
        self.z13.setText("{}".format(self.n2 / self.n4))
        self.z14.setText("{}".format(self.n5 / self.n6))
        self.z15.setText("{}".format(self.n1 / self.n7))
       
    def go1(self):
       k = self.y1.text()
       self.xy1.setEnabled(False)
       if int(k) == self.n2 / self.n1:
           self.correct += 1
           self.count1 += 1
           self.ok1.display(self.count1)
           pal = self.z1.palette()
           pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
           self.z1.setPalette(pal)
       else:
           self.count2 += 1
           self.ok2.display(self.count2)
           
    def go2(self):
        k = self.y2.text()
        self.xy2.setEnabled(False)
        if int(k) == self.n3 / self.n4:
           self.correct += 1
           self.count1 += 1
           self.ok1.display(self.count1)
           pal = self.z2.palette()
           pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("red"))
           self.z2.setPalette(pal)
        else:
           self.count2 += 1
           self.ok2.display(self.count2)
           
    def go3(self):
        k = self.y3.text()
        self.xy3.setEnabled(False)
        if int(k) == self.n5 / self.n2:
           self.correct += 1
           self.count1 += 1
           self.ok1.display(self.count1)
           pal = self.z3.palette()
           pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("blue"))
           self.z3.setPalette(pal)
        else:
           self.count2 += 1
           self.ok2.display(self.count2)
           
    def go4(self):
        k = self.y4.text()
        self.xy4.setEnabled(False)
        if int(k) == self.n1 / self.n3:
           self.correct += 1
           self.count1 += 1
           self.ok1.display(self.count1)
           pal = self.z4.palette()
           pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor("green"))
           self.z4.setPalette(pal)
        else:
           self.count2 += 1
           self.ok2.display(self.count2)
           
           
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main() 
    ex.show() 
    sys.exit(app.exec())
          
      
        
        
        
        
          
       
       
       
       
       
       
