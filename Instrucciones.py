# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'NuevoProyecto.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Instrucciones(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(931, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        self.titulo.setGeometry(QtCore.QRect(350, 20, 301, 81))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(15)
        self.titulo.setFont(font)
        self.titulo.setObjectName("titulo")

        self.b_return = QtWidgets.QPushButton(self.centralwidget)
        self.b_return.setGeometry(QtCore.QRect(0, 660, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b_return.setFont(font)
        self.b_return.setObjectName("b_return")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 704, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Instrucciones"))
        self.titulo.setText(_translate("MainWindow", "Instrucciones"))
        self.b_return.setText(_translate("MainWindow", "Back"))


# Para correr solo esta ventana
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Instrucciones()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
