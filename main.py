from modelo import TorresDeHanoi
import sys
from PyQt6.QtWidgets import QApplication

# Este es el punto de entrada de la aplicación
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TorresDeHanoi()
    ventana.show()
    sys.exit(app.exec())