from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtUiTools import *
from modules.crawler import *
import threading
class Test(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = QUiLoader().load('main.ui',self)
        self.main.btnscan.clicked.connect(self.Sthread)
        self.main.show()
    def Sthread(self):
        t = threading.Thread(target=self.show)
        t.start()
    def show(self):
        listscan=self.main.listscan
        url=self.main.lineurl.text()
        print(url)
        m=crawler_links(url,100)
        for i in m:
            item=QListWidgetItem(i,listscan)
app=QApplication()
frame=Test()
app.exec_()

