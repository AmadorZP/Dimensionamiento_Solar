import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QDialog, QApplication


class programa(QDialog): #nombre de la app

    def __init__(self):
        super().__init__() #va siempre
        uic.loadUi("gui_app.ui", self)
        self.boton_desactivar.setEnabled(False) #botones
        self.boton_activar.clicked.connect(self.fn_activar)
        self.boton_desactivar.clicked.connect(self.fn_desactivar)

    def fn_activar(self):
        self.boton_desactivar.setEnabled(True)
        self.boton_activar.setEnabled(False)
        self.etiqueta.setText("ACTIVADO")

    def fn_desactivar(self):
        self.boton_desactivar.setEnabled(False)
        self.boton_activar.setEnabled(True)
        self.etiqueta.setText("DESACTIVADO")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = programa()
    GUI.show()
    sys.exit(app.exec_())
