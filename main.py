from ast import Lambda
from PyQt6 import QtCore, QtGui, QtWidgets, QtWidgets, uic,QtGui
from ui_dlcalc_gui import Ui_MainWindow
import sys
import numpy as np


class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.calculateButton.clicked.connect(lambda: self.calculate())
        
        
    def calculate(self):
        self.fileSize = float(self.fileSizeEntry.text())
        self.dlSpeed = float(self.dlSpeedEntry.text())
        dlTime=( ( self.fileSize ) * 8 * 1024) / ( self.dlSpeed )
        dlTime_hr = float(np.floor( dlTime / 3600 ))
        dlTime_min = float(np.floor( ( dlTime - ( dlTime_hr*3600 ) ) / 60 ))
        dlTime_sec = float(np.floor( ( dlTime - ( dlTime_hr*3600 ) - dlTime_min*60)  ))
        self.label_6.setText(f"{int(dlTime_hr)} Hours, {int(dlTime_min)} Minutes, and {int(dlTime_sec)} Seconds")    
    
        

        
def main():    
    app = QtWidgets.QApplication(sys.argv)
    #mainWindow = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    
    sys.exit(app.exec())



 
if __name__ == "__main__":
    main()