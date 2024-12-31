import sys
from PyQt5.QtWidgets import QApplication
from interface import AppWindow

if __name__ == "__main__":      
    app = QApplication(sys.argv)
    janela = AppWindow()
    janela.show()
    sys.exit(app.exec_())