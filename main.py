from controlador import TorresDeHanoi
import sys
from PyQt6.QtWidgets import QApplication
from modelo import Base, engine  # Importar el modelo y el motor de SQLAlchemy

# Este es el punto de entrada de la aplicación
if __name__ == "__main__":

    Base.metadata.create_all(engine)  # Crear las tablas en la base de datos

    app = QApplication(sys.argv)
    ventana = TorresDeHanoi()
    ventana.show()
    sys.exit(app.exec())