import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from saa import Ui_Form
from chit import Ui_chit
from bibl import Ui_bibl

def main():
    app = QtWidgets.QApplication(sys.argv)
    window_ui = Ui_Form()
    window = QtWidgets.QMainWindow()
    window_ui.setupUi(window)
    window.show()
    #chit
    chit_ui = Ui_chit()
    chit = QtWidgets.QWidget()
    chit_ui.setupUi(chit)
    window_ui.pushButton_6.clicked.connect(lambda:chit.show())
    #bibl
    bibl_ui = Ui_bibl()
    bibl = QtWidgets.QWidget()
    bibl_ui.setupUi(bibl)
    window_ui.pushButton_5.clicked.connect(lambda:bibl.show())
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()


