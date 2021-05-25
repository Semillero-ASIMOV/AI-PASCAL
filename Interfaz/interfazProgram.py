import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow , QApplication
class interfaz_GUI (QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI_interfaz.ui",self)
        self.directores.clicked.connect(self.fn_directores)
        self.decanos.clicked.connect(self.fn_decanos)
        self.bienestar.clicked.connect(self.fn_bienestar)
        self.rectoria.clicked.connect(self.fn_rectoria)

    def fn_directores(self):
        self.etiqueta.setText("Georffrey Acevedo Gonzalez - Ing. Mecatrónica (oficina... bloque c)""\n"
                              "Carolina Castaño - Ing.Biomédica (oficina ... bloque c")

    def fn_bienestar(self):
        self.etiqueta.setText("Pedro Nel Orozco- Asistente de bienestar""\n"
                              "correo: pedro.orozcoeia.edu.co")

    def fn_decanos(self):
        self.etiqueta.setText("decanos..")

    def fn_rectoria(self):
        self.etiqueta.setText("Carlos Felipe Londoño Alvárez - Rector""\n""(oficina.. piso 2)")

if __name__=='__main__':
    app = QApplication(sys.argv)
    GUI = interfaz_GUI()
    GUI.show()
    sys.exit(app.exec_())
