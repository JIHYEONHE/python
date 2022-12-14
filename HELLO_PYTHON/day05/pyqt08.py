import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from random import random
#홀짝 게임!!!!!!
form_class = uic.loadUiType("pyqt08.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.myclick)
        self.le_mine.returnPressed.connect(self.myclick) #엔터키 누르면 돌아가게 해주는것!       
    

    def myclick(self):
        mine = self.le_mine.text()
        com =""
        result =""
        
        rnd = random() #랜덤 1까지의 임의의 소수
        if rnd > 0.66:
            com ="가위"
        elif rnd> 0.33:
            com="바위"
        else:
            com="보"
            
        if com == "가위" and mine == "가위": result = "비김"
        if com == "가위" and mine == "바위": result = "승리"
        if com == "가위" and mine == "보": result = "패배"
        
        if com == "바위" and mine == "가위": result = "짐"
        if com == "바위" and mine == "바위": result = "비김"
        if com == "바위" and mine == "보": result = "승리"
        
        if com == "보" and mine == "가위": result = "승리"
        if com == "보" and mine == "바위": result = "패배"
        if com == "보" and mine == "보": result = "비김"
        
        self.le_com.setText(com)
        self.le_result.setText(result)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()