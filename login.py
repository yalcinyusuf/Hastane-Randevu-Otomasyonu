import sys 
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
from PyQt5 import uic
from main import mainApp

USERNAME ='admin'
PASSWORD = 'myPassword'
class loginApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Uis/login.ui',self)
        self.login_Btn.clicked.connect(self.checkLogin)
        self.w = None
    def errorBox(self,hataMesaji=str)->None:
        """[Ekrana hata mesaji yansitir.]

        Args:
            hataMesaji ([string], optional): [Ekranda gosterilecek hata mesaji]. Defaults to str.
        """        
        errorBox= QMessageBox(self)
        errorBox.setStyleSheet('background-color: rgb(255, 255, 255);color:(100,100,100);')
        errorBox.setText(hataMesaji)
        errorBox.show()
        
    def checkLogin(self):
        if(self.username_Line.text()==USERNAME):
            
            if(self.pass_Line.text()== PASSWORD):
                if self.w is None:
                
                    self.close()
                    self.w = mainApp()
            else:
                self.errorBox('Hatali Sifre Girdiniz !')
        else:
            self.errorBox('Hatali Kullanici Adi Girdiniz !')
        

app = QApplication(sys.argv)
demo = loginApp()
demo.show()
try:
    sys.exit(app.exec_())
except SystemExit:
    print('Closing Window')



# def showDialog():
#    msgBox = QMessageBox()
#    msgBox.setIcon(QMessageBox.Information)
#    msgBox.setText("Message box pop up window")
#    msgBox.setWindowTitle("QMessageBox Example")
#    msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msgBox.buttonClicked.connect(msgButtonClick)

#    returnValue = msgBox.exec()
#    if returnValue == QMessageBox.Ok:
#       print('OK clicked')