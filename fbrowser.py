# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cargararchivos.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def browsefiles(self, window):
        fname = QtWidgets.QFileDialog.getOpenFileName(window, "Escoge archivo", "C:\ Users")
        self.filename.setText(fname[0])

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 450)
        self.filename = QtWidgets.QLineEdit(Dialog)
        self.filename.setGeometry(QtCore.QRect(60, 160, 211, 31))
        self.filename.setObjectName("filename")
        # Botones
        self.b_browse = QtWidgets.QPushButton(Dialog)
        self.b_browse.setGeometry(QtCore.QRect(310, 160, 91, 31))
        self.b_browse.setObjectName("b_browse")
        self.b_browse.clicked.connect(lambda: self.browsefiles(Dialog))

        self.b_return = QtWidgets.QPushButton(Dialog)
        self.b_return.setGeometry(QtCore.QRect(0, 400, 61, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b_return.setFont(font)
        self.b_return.setObjectName("b_return")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cargar Proyecto"))
        self.b_browse.setText(_translate("Dialog", "Buscar..."))
        self.b_return.setText(_translate("MainWindow", "Back"))


# Para correr solo esta ventana
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
